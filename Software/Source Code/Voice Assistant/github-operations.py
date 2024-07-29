# github_operations.py
from github import Github

def authenticate_github(token):
    """Authenticate to GitHub."""
    g = Github(token)
    return g

def get_repo_info(g, repo_name):
    """Retrieve information about a repository."""
    repo = g.get_repo(repo_name)
    return repo

def list_repo_files(g, repo_name):
    """List all files in the repository."""
    repo = g.get_repo(repo_name)
    contents = repo.get_contents("")
    files = []
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            files.append(file_content.path)
    return files

def get_file_content(g, repo_name, file_path):
    """Get the content of a specific file."""
    repo = g.get_repo(repo_name)
    file_content = repo.get_contents(file_path)
    return file_content.decoded_content.decode()

# Example usage:
# token = "your_personal_access_token"
# g = authenticate_github(token)
# repo_info = get_repo_info(g, "repository_owner/repository_name")
# files = list_repo_files(g, "repository_owner/repository_name")
# content = get_file_content(g, "repository_owner/repository_name", "path/to/file")
