import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from dotenv import load_dotenv

from agent_components.planner_agent import make_plan
from agent_components.self_critic_agent import critique_plan, improve_plan
from agent_components.tool_agent import tool_call_for_debt_ratio
from agent_components.safety_wrapper import safe_input

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_PATH = BASE_DIR / "templates" / "index.html"


def calculate_debt_ratio(income, existing_debt, loan_amount):
    if income <= 0:
        return None
    return round((existing_debt + loan_amount) / income, 2)


def fairness_audit(profile):
    protected_fields = ["age", "gender", "marital_status", "ethnicity", "nationality"]
    present = [field for field in protected_fields if field in profile and profile[field]]
    return {
        "protected_fields_seen": present,
        "audit_note": "Decision factors should be based on financial capacity and policy rules, not protected attributes."
    }


def build_prompt(profile, scenario=None):
    base = profile.copy()
    if scenario:
        base.update(scenario)

    income = base.get("income", 0)
    debt = base.get("existing_debt", 0)
    loan = base.get("loan_amount", 0)
    debt_ratio = calculate_debt_ratio(income, debt, loan)

    prompt = f"""
You are a responsible credit-risk underwriting assistant.
Your task is to give an explainable, auditable decision-support assessment for a loan applicant.

Applicant profile:
- Name: {base.get('name', 'Applicant')}
- Annual income: {income}
- Existing debt: {debt}
- Requested loan amount: {loan}
- Credit score: {base.get('credit_score', 'unknown')}
- Employment status: {base.get('employment_status', 'unknown')}
- Loan purpose: {base.get('loan_purpose', 'unknown')}
- Debt-to-income ratio (estimated): {debt_ratio if debt_ratio is not None else 'unknown'}

Rules:
- Do not make a final approval decision as a black box.
- Explain the reasoning in clear, plain language.
- Mention the key financial factors.
- Include a fairness audit note that says protected characteristics should not be used as direct credit factors.
- Return valid JSON with fields: risk_level, recommendation, rationale, key_factors, fairness_audit, what_if_summary, applicant_letter.
"""
    return prompt


def fallback_assessment(profile, draft_plan, critique, improved_plan, tool_result):
    debt_ratio = calculate_debt_ratio(
        profile.get("income", 0),
        profile.get("existing_debt", 0),
        profile.get("loan_amount", 0),
    )
    risk_level = "low" if debt_ratio is not None and debt_ratio <= 0.5 else "medium"
    if debt_ratio is not None and debt_ratio > 0.8:
        risk_level = "high"

    return {
        "risk_level": risk_level,
        "recommendation": "Proceed with manual review" if risk_level != "low" else "Recommend proceeding",
        "rationale": f"Planner: {draft_plan}\nCritique: {critique}\nImproved plan: {improved_plan}\nTool result: {tool_result}",
        "key_factors": [
            f"Estimated debt-to-income ratio: {debt_ratio}" if debt_ratio is not None else "Debt-to-income ratio unavailable",
            f"Credit score: {profile.get('credit_score', 'unknown')}",
            f"Employment status: {profile.get('employment_status', 'unknown')}"
        ],
        "fairness_audit": fairness_audit(profile),
        "what_if_summary": ["Scenario simulation is available; adjust income, debt, and loan amount to see how the risk changes."],
        "applicant_letter": "Dear Applicant, thank you for your application. Your request has been reviewed using explainable financial factors and a fairness review."
    }


def get_assessment(profile, scenario=None):
    safe_profile = safe_input(json.dumps(profile))
    if not safe_profile["allowed"]:
        return {
            "risk_level": "high",
            "recommendation": "Blocked for safety review",
            "rationale": "Input was blocked by the safety wrapper.",
            "key_factors": ["Input safety review failed"],
            "fairness_audit": fairness_audit(profile),
            "what_if_summary": [],
            "applicant_letter": ""
        }

    goal = f"Assess loan risk for {profile.get('name', 'Applicant')} using explainable underwriting reasoning."

    try:
        draft_plan = make_plan(goal)
        critique = critique_plan(goal, draft_plan)
        improved_plan = improve_plan(goal, draft_plan, critique)
    except Exception:
        draft_plan = "Fallback planning step"
        critique = "Fallback critique"
        improved_plan = "Fallback improvement"

    try:
        tool_result = tool_call_for_debt_ratio(
            profile.get("income", 0),
            profile.get("existing_debt", 0),
            profile.get("loan_amount", 0),
        )
    except Exception:
        tool_result = "tool unavailable"

    if os.getenv("OPENAI_API_KEY"):
        prompt = build_prompt(profile, scenario)
        try:
            from openai import OpenAI
            client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
                response_format={"type": "json_object"},
            )
            content = response.choices[0].message.content
            data = json.loads(content)
        except Exception:
            data = {}
    else:
        data = {}

    if not data:
        return fallback_assessment(profile, draft_plan, critique, improved_plan, tool_result)

    data.setdefault("fairness_audit", fairness_audit(profile))
    data.setdefault("what_if_summary", [])
    data.setdefault("applicant_letter", "")
    return data


class CreditRiskHandler(BaseHTTPRequestHandler):
    def _send_text(self, text, status=200, content_type="text/html; charset=utf-8"):
        body = text.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path in {"/", "/index.html"}:
            if TEMPLATE_PATH.exists():
                self._send_text(TEMPLATE_PATH.read_text(encoding="utf-8"))
            else:
                self._send_text("Template not found", status=404)
            return
        self._send_text("Not found", status=404)

    def do_POST(self):
        if self.path != "/assess":
            self._send_text("Not found", status=404)
            return

        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length).decode("utf-8") if length else "{}"
        data = json.loads(body or "{}")
        profile = data.get("profile", {})
        scenario = data.get("scenario", None)
        response = get_assessment(profile, scenario)

        payload = json.dumps(response).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, format, *args):
        return


def run_server():
    server = ThreadingHTTPServer(("127.0.0.1", 5001), CreditRiskHandler)
    print("Serving at http://127.0.0.1:5001")
    server.serve_forever()


if __name__ == "__main__":
    run_server()
