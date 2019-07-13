import logging

from git import Repo
from git.exc import InvalidGitRepositoryError


def git_info(working_dir):
    with Repo(working_dir) as repo:
        if not repo.bare:
            branch = repo.head.reference.name
            tree_diff = repo.head.commit.diff(None)
            return branch, len(tree_diff)


def is_git_dir(working_dir):
    try:
        Repo(working_dir)
        return True
    except InvalidGitRepositoryError:
        return False


def create_feature_branch(working_dir, source_branch, new_branch):
    with Repo(working_dir) as repo:
        git = repo.git
        stash_out = git.stash("push")
        logging.debug("Git stash push")
        logging.debug(stash_out)
        repo.head.set_reference(repo.heads[source_branch])
        new_branch = repo.create_head(new_branch)
        new_branch.checkout()


def apply_stash(working_dir):
    with Repo(working_dir) as repo:
        git = repo.git
        stash_out = git.stash("pop")
        logging.debug("Git stash pop")
        logging.debug(stash_out)
