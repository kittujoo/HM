import os
import subprocess
from subprocess import Popen, PIPE
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))


def get_repo_commit_id(repo_folder_path) -> str:
    """
    Common utility to get the latest commit id based on Repo folder path
    :return: git commit id
    """
    return Popen('git log --format="%H" -n 1', shell=True, stdout=PIPE, cwd=repo_folder_path).stdout.read().decode().strip()


def checkout_repo_commit_id(repo_commit_id, repo_directory):
    """
    Checkout to a specific version
    """
    git_log_cmd = subprocess.run(["git", "log"], stdout=subprocess.PIPE, text=True, cwd=repo_directory)
    output_git_log_cmd = git_log_cmd.stdout
    if repo_commit_id not in output_git_log_cmd:
        logger.info(f"Version = {repo_commit_id} NOT found in repo log file")
        raise ValueError(f"Please check requested repository version value. Supplied version = {repo_commit_id} NOT found in repository log file")

    logger.debug(f"Checking out ref: {repo_commit_id} of the repository")
    subprocess.run(["git", "checkout", repo_commit_id], stdout=subprocess.PIPE, text=True, shell=True, cwd=repo_directory)
    logger.debug("Completed checkout of specific repo version")