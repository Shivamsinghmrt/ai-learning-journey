def critique_plan(goal: str, plan: str) -> str:
    return f"Potential issue: the plan should explicitly include fairness and explanation checks for: {goal}"


def improve_plan(goal: str, plan: str, critique: str) -> str:
    return f"{plan}\n4. Add fairness and explainability review. 5. Produce a clear applicant-facing summary for: {goal}"
