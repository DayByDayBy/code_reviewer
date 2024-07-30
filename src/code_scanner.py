# rough sketch, will fill out later and join it all up once it's actually needed



from typing import List, Dict, Any
import ollama

def get_llm_suggestions(code: str) -> List[str]:
    suggestions = ollama.generate(model='llama3', prompt=code)
    return suggestions

def analyse_code(code: str) -> Dict[str, Any]:
    if not code:
        return {'error': 'No code provided'}
    try:
        complexity = calculate_complexity(code)
        suggestions = get_llm_suggestions(code)
        return {'complexity': complexity, 'suggestions': suggestions}
    except Exception as e:
        return {'error': str(e)}

def calculate_complexity(code: str) -> int:
    complexity = 0
    lines = code.split('\n')
    for line in lines:
        if 'if' in line or 'for' in line or 'while' in line:
            complexity += 1
    return complexity
