import pytest, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from engine.rubric_registry import RubricRegistry

def test_rubric_registry_count():
    reg = RubricRegistry()
    rubrics = reg.list_rubrics()
    assert len(rubrics) == 18, f"Expected 18 rubrics, found {len(rubrics)}"

def test_scoring_functionality():
    reg = RubricRegistry()
    res = reg.evaluate_simple("math_step_by_step_reasoning", "Solve 2x=10", "x=5")
    assert res['score'] == 5
    assert res['rubric_id'] == "math_step_by_step_reasoning"
