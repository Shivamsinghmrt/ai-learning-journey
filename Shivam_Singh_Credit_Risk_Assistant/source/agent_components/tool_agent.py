def tool_call_for_debt_ratio(income: float, existing_debt: float, loan_amount: float) -> str:
    if income <= 0:
        return "Income must be positive"
    ratio = round((existing_debt + loan_amount) / income, 2)
    return f"Debt-to-income ratio is {ratio}"
