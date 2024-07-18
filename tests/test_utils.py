import pytest

from src.utils import analyse_code

@pytest.fixture
def sample_code():
    return"""
    def calculate_sum(a,b):
        return a + b
    def calculate_product(a, b):
        return a * b
    """
    
def test_analyse_code_with_fixture(sample_code):
    result = analyse_code(sample_code)
    assert 'complexity' in result
    assert 'suggestion' in result 
    assert len(result['suggestions']) > 0

@pytest.fixture
def mock_llm_response(monkeypatch):
    def mock_get_llm_suggestions(*args, **kwargs):
        return ["use type hinsts", "add docstrings"]
    monkeypatch.setattr('src.utils.get_llm_suggestions', mock_get_llm_suggestions)

def test_analyse_code_with_mock_llms(sample_code, mock_llm_response):
    result = analyse_code(sample_code)
    assert "use type hints" in result['suggestions']
    assert "add docstrings" in result['suggestions']
    
    
    
    
    
    
    
# def test_analyse_code():
#     code = "def greet(name):\n  return f'Hello, {name}!'"
#     result = analyse_code(code)
#     assert isinstance(result, dict)
#     assert 'complexity' in result
#     assert 'suggestions' in result



# @pytest.mark.parametrize("code, expected complexity", [
#     ("def simple():\n    pass", 1),
#     ("def complex(x):\n    if x:\n        return True\n    else:\n        return False", 2)
# ])

# def test_code_complexity(code, expected_complexity):
#     result = analyse_code(code)
#     assert result['complexity'] == expected_complexity