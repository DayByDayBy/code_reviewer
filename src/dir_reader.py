# rough sketch, will fill out later and join it all up once it's actually needed


import os

def read_code_from_directory(directory: str) -> str:
    code = ""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file), 'r') as f:
                    code += f.read() + '\n'
    return code
