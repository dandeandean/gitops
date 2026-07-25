#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "gitpython>=3.1.50",
#     "pyyaml>=6.0.3",
# ]
# ///

from git import Repo
import yaml
import os, sys


def git_root_path() -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Find the repository root by searching upward
    repo = Repo(script_dir, search_parent_directories=True)
    root_dir = repo.working_tree_dir
    if not root_dir:
        return ""
    return str(root_dir)

def find_kust_paths() -> list[str]:
    ''' Returns all of the kustomization.yaml files in the git tree'''
    if git_root_path == "":
        return []
    walker = os.walk(git_root_path())
    kust_paths : list[str] = []
    for path, _, files in walker:
        if "kustomization.yaml" in files:
            kust_path = os.path.join(path,"kustomization.yaml")
            kust_paths.append(kust_path)
    return kust_paths


def check_kust(path_to: str) -> bool:
    ''' Return True if the kustomization seems okay'''
    print("checking:", path_to)
    result_code = True
    with open(path_to, "r") as file:
        resources  = yaml.safe_load(file).get("resources") or []
        for resource in resources:
            resource_path = os.path.join(os.path.dirname(path_to),resource)
            path_there = os.path.exists(resource_path)
            if not path_there:
                result_code = False
            print(f"\t{resource_path} -- {path_there}")
    return result_code

def main(_: list[str]) -> int:
    exit_code = 0
    for k in find_kust_paths():
        if not check_kust(k):
            exit_code = 1
    return exit_code


if __name__ == "__main__":
    sys.exit(main(sys.argv))
