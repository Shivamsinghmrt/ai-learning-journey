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


def build_scenario_summary(profile, scenario=None):
    if not scenario:
        return ["No what-if scenario provided."]

    base_ratio = calculate_debt_ratio(
        profile.get("income", 0),
        profile.get("existing_debt", 0),
        profile.get("loan_amount", 0),
    )
    scenario_ratio = calculate_debt_ratio(
        scenario.get("income", profile.get("income", 0)),
        scenario.get("existing_debt", profile.get("existing_debt", 0)),
        scenario.get("loan_amount", profile.get("loan_amount", 0)),
    )

    if base_ratio is None or scenario_ratio is None:
        return ["Scenario summary unavailable."]

    change = round(scenario_ratio - base_ratio, 2)
    direction = "improves" if scenario_ratio < base_ratio else "worsens"
    return [
        f"Base debt-to-income ratio: {base_ratio}.",
        f"Scenario debt-to-income ratio: {scenario_ratio}.",
        f"Change: {change}. This scenario {direction} the repayment burden.",
    ]


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
- What-if scenario: {scenario if scenario else 'none'}

Rules:
- Do not make a final approval decision as a black box.
- Explain the reasoning in clear, plain language.
- Mention the key financial factors.
- Include a fairness audit note that says protected characteristics should not be used as direct credit factors.
- Return valid JSON with fields: risk_level, recommendation, rationale, key_factors, fairness_audit, what_if_summary, applicant_letter.
"""
    return prompt


def build_local_assessment(profile, scenario=None):
    base_income = profile.get("income", 0)
    base_debt = profile.get("existing_debt", 0)
    base_loan = profile.get("loan_amount", 0)
    base_ratio = calculate_debt_ratio(base_income, base_debt, base_loan)
    credit_score = profile.get("credit_score", 0)

    risk_score = 0
    if base_ratio is None:
        risk_score = 1
    elif base_ratio <= 0.50:
        risk_score = -1
    elif base_ratio <= 0.80:
        risk_score = 0
    else:
        risk_score = 1

    if credit_score >= 750:
        risk_score -= 1
    elif credit_score < 650:
        risk_score += 1

    if base_loan > base_income * 0.6:
        risk_score += 1

    if risk_score <= -1:
        risk_level = "Low"
        recommendation = "Recommend proceeding with standard monitoring"
    elif risk_score == 0:
        risk_level = "Moderate"
        recommendation = "Further review recommended"
    else:
        risk_level = "High"
        recommendation = "Escalate for deeper review"

    scenario_summary = build_scenario_summary(profile, scenario)
    scenario_income = scenario.get("income", base_income) if scenario else base_income
    scenario_debt = scenario.get("existing_debt", base_debt) if scenario else base_debt
    scenario_loan = scenario.get("loan_amount", base_loan) if scenario else base_loan
    scenario_ratio = calculate_debt_ratio(scenario_income, scenario_debt, scenario_loan)

    return {
        "risk_level": risk_level,
        "recommendation": recommendation,
        "rationale": (
            f"The assessment uses the applicant's income, existing debt, requested loan amount, and credit score. "
            f"The base debt-to-income ratio is {base_ratio}. "
            f"The scenario debt-to-income ratio is {scenario_ratio}. "
            f"This makes the scenario impact explicit and explainable."
        ),
        "key_factors": {
            "annual_income": base_income,
            "existing_debt": base_debt,
            "requested_loan_amount": base_loan,
            "credit_score": credit_score,
            "debt_to_income_ratio": base_ratio,
            "scenario_debt_to_income_ratio": scenario_ratio,
        },
        "fairness_audit": fairness_audit(profile),
        "what_if_summary": scenario_summary,
        "applicant_letter": (
            f"Dear {profile.get('name', 'Applicant')},\n\n"
            f"Thank you for your application. Your request was reviewed using explainable financial factors. "
            f"The current debt-to-income ratio is {base_ratio} and the what-if scenario produces a debt-to-income ratio of {scenario_ratio}."
        ),
    }


def fallback_assessment(profile, draft_plan, critique, improved_plan, tool_result, scenario=None):
    return build_local_assessment(profile, scenario)


def get_assessment(profile, scenario=None):
    safe_profile = safe_input(json.dumps(profile))
    if not safe_profile["allowed"]:
        return {
            "risk_level": "High",
            "recommendation": "Blocked for safety review",
            "rationale": "Input was blocked by the safety wrapper.",
            "key_factors": ["Input safety review failed"],
            "fairness_audit": fairness_audit(profile),
            "what_if_summary": build_scenario_summary(profile, scenario),
            "applicant_letter": ""
        }

    try:
        draft_plan = make_plan(f"Assess loan risk for {profile.get('name', 'Applicant')}")
        critique = critique_plan(f"Assess loan risk for {profile.get('name', 'Applicant')}", draft_plan)
        improved_plan = improve_plan(f"Assess loan risk for {profile.get('name', 'Applicant')}", draft_plan, critique)
    except Exception:
        draft_plan = "Fallback planning step"
        critique = "Fallback critique"
        improved_plan = "Fallback improvement"

    return build_local_assessment(profile, scenario)


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