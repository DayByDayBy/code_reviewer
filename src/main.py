#  maybe main.py, maybe modular, maybe semi? full on could be overkill, even tho some of the bits might be of repeate use


# import os
# import json
# from typing import List, Dict, Any
# from git import Repo
# from datetime import datetime

# def clone_repo(repo_url: str, clone_dir: str) -> str:
#     if not os.path.exists(clone_dir):
#         os.makedirs(clone_dir)
#     repo_path = os.path.join(clone_dir, os.path.basename(repo_url))
#     if not os.path.exists(repo_path):
#         Repo.clone_from(repo_url, repo_path)
#     return repo_path

# def read_code_from_directory(directory: str) -> str:
#     code = ""
#     for root, _, files in os.walk(directory):
#         for file in files:
#             if file.endswith('.py'):
#                 with open(os.path.join(root, file), 'r') as f:
#                     code += f.read() + '\n'
#     return code

# def get_llm_suggestions(code: str) -> List[str]:
#     # Placeholder for actual ollama.generate() method
#     return ollama.generate(model='llama3', prompt=code)

# def calculate_complexity(code: str) -> int:
#     complexity = 0
#     lines = code.split('\n')
#     for line in lines:
#         if 'if' in line or 'for' in line or 'while' in line:
#             complexity += 1
#     return complexity

# def analyse_code(code: str) -> Dict[str, Any]:
#     if not code:
#         return {'error': 'No code provided'}
#     try:
#         complexity = calculate_complexity(code)
#         suggestions = get_llm_suggestions(code)
#         return {'complexity': complexity, 'suggestions': suggestions}
#     except Exception as e:
#         return {'error': str(e)}

# def save_analysis(analysis: Dict[str, Any], filename: str) -> None:
#     timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
#     with open(f"{filename}_{timestamp}.json", 'w') as f:
#         json.dump(analysis, f, indent=4)

# def main(repo_url: str, clone_dir: str, save_filename: str) -> None:
#     repo_path = clone_repo(repo_url, clone_dir)
#     code = read_code_from_directory(repo_path)
#     analysis = analyse_code(code)
#     save_analysis(analysis, save_filename)

# if __name__ == "__main__":
#     REPO_URL = 'https://github.com/your/repo.git'
#     CLONE_DIR = 'cloned_repos'
#     SAVE_FILENAME = 'analysis_results'
#     main(REPO_URL, CLONE_DIR, SAVE_FILENAME)
