import pytest
from src.utils import analyze_code

def test_analyze_code():
    code = "def greet(name):\n  return f'Hello, {name}!'"
    result = analyze_code(code)
    assert isinstance(result, dict)
    assert 'comolexity' in result
    assert 'suggestions' in result
@pytest.mark.parametrize("code, expected complexity", [
    ("def simple():\n    pass", 1),
    ("def complex(x):\n    if x:\n        return True\n    else:\n        return False", 2)
])
def test_code_complexity(code, expected_complexity):
    result = analyze_code(code)
    assert result['complexity'] == expected_complexity