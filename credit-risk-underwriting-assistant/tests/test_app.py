import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app import TEMPLATE_PATH, calculate_debt_ratio, fairness_audit, get_assessment


def test_debt_ratio_calculation():
    assert calculate_debt_ratio(100000, 20000, 30000) == 0.5


def test_fairness_audit_includes_note():
    result = fairness_audit({"age": 32, "gender": "female"})
    assert "protected_fields_seen" in result
    assert "audit_note" in result


def test_get_assessment_falls_back_without_openai_key():
    result = get_assessment({"income": 100000, "existing_debt": 20000, "loan_amount": 30000, "credit_score": 720})
    assert result["risk_level"] in {"low", "medium", "high"}
    assert "recommendation" in result


def test_index_template_exists():
    assert TEMPLATE_PATH.exists()


def test_scenario_changes_are_reflected_in_summary():
    result = get_assessment(
        {"income": 100000, "existing_debt": 20000, "loan_amount": 30000, "credit_score": 720},
        {"income": 150000, "existing_debt": 10000, "loan_amount": 10000},
    )
    assert "what_if_summary" in result
    assert any("150000" in item for item in result["what_if_summary"])
