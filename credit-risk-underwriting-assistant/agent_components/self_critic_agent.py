import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask(system: str, user: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
    )
    return response.choices[0].message.content


def critique_plan(goal: str, draft_plan: str) -> str:
    return ask(
        "You are a critical reviewer for loan underwriting decisions. List concrete risks, gaps, and missing steps.",
        f"Goal: {goal}\n\nPlan:\n{draft_plan}",
    )


def improve_plan(goal: str, draft_plan: str, critique: str) -> str:
    return ask(
        "You are a planning agent. Rewrite the plan so it fixes every issue in the critique.",
        f"Goal: {goal}\n\nOriginal plan:\n{draft_plan}\n\nCritique:\n{critique}",
    )
