# rough sketch, will fill out later and join it all up once it's actually needed


import os
from git import Repo

def clone_repo(repo_url: str, clone_dir: str) -> str:
    if not os.path.exists(clone_dir):
        os.makedirs(clone_dir)
    repo_path = os.path.join(clone_dir, os.path.basename(repo_url))
    if not os.path.exists(repo_path):
        Repo.clone_from(repo_url, repo_path)
    return repo_path


