"""Write a YAML file for the Voight-Kampff test setup script.

Voight-Kampff is the name of the integration test suite for mycroft-core and
mycroft-skills.  The test setup script installs the skills to include in the
test and copies their feature files over to core for inclusion in the tests.
"""
from argparse import ArgumentParser
from os import environ

import requests
from github import Github


def parse_command_line():
    """Get the values of the command line arguments."""
    arg_parser = ArgumentParser()
    arg_parser.add_argument(
        "--pull-request",
        default=None,
        help='The Pull Request to be tested.'
    )
    arg_parser.add_argument(
        "--platform",
        default='mycroft_mark_1',
        help='The Pull Request to be tested.'
    )

    return arg_parser.parse_args()


def get_pull_request_diff(args):
    """Get the difference between the base branch and the modified branch."""
    pr_number = int(args.pull_request.strip('PR-'))
    g = Github(environ['GITHUB_API_KEY'])
    repo = g.get_repo('MycroftAI/mycroft-skills')
    pr = repo.get_pull(pr_number)
    pr_diff = requests.get(pr.diff_url)

    return pr_diff.text.split('\n')


def get_pull_request_submodule(pull_request_diff):
    """Determine the submodule name of the skill added/modified in the PR"""
    diff_file_name = None
    skill_submodule_name = None
    for line in pull_request_diff:
        #  The line indicating the file being compared looks like this:
        #    diff --git a/<file name> b/<file name>
        if line.startswith('diff --git a/'):
            words = line.split()
            diff_file_name = words[2].strip('a/')
        # If a file contains a subproject commit hash it represents a skill
        if line.startswith('+Subproject commit '):
            skill_submodule_name = diff_file_name
            break

    return skill_submodule_name


def write_test_config_file(skill_submodule_name):
    """Write a YAML file for the integration test setup script

    Not every PR into this repository will be a change to a skill.  If no
    skill submodule was found in the PR, just add the "hello world" skill.
    """
    if skill_submodule_name is None:
        submodule = 'skill-hello-world'
    else:
        submodule = skill_submodule_name
    with open('test_skill.yml', 'w') as config_file:
        config_file.write('test_skills:\n')
        config_file.write('- ' + submodule + '\n')


def main():
    args = parse_command_line()
    pull_request_diff = get_pull_request_diff(args)
    skill_submodule_name = get_pull_request_submodule(pull_request_diff)
    write_test_config_file(skill_submodule_name)


if __name__ == '__main__':
    main()
