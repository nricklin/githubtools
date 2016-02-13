from setuptools import setup, find_packages
import textwrap

setup(name='githubtools',
      version='0.3.0',
      author='nricklin',
      author_email='nricklin@digitalglobe.com',
      license='MIT',
      description='Some simple commandline tools for interacting with github: status, merge, pull, etc.',
      long_description=textwrap.dedent("""\
			Some commandline tools for interacting with github.
			=====================

			Things you can do:
			- Set commit status
			- Create a pull request
			- Merge a pull request
			- Merge

			Set Status on a commit:

				Usage:
					github-commit-status -c <commit-hash> -s <status> -u <github-username> -p <github-password> -r <github_repo> --url <URL> --context <context> -d "<description>"
					github-commit-status -c <commit-hash> -s <status> -t <github-token> -r <github_repo> --url <URL> --context <context> -d "<description>"

				Options:
					-c <commit-hash>, --commit-hash <commit-hash>  Github commit hash
					-s <status>, --status <status>  Status to set [pending, success, error, or failure]
					-u <username>, --username <username>  github username
					-p <password>, --password <password>  github password
					-t <token>, --token <token>  github access token
					-r <repository>, --repo <repository> github repository
					-d <description> --description <description> description of the status
					--url <url> URL to refer back to
					--context <context> The context of the status.  Typically the name of the service creating the status.


			Create a pull request:

				Usage:
					github-create-pull-request -h <head> -b <base> -t <token> -r <repo> [-d "<description>" --title <title>]

				Options:
					-h <head>, --head <head>  Head: the branch you're pulling from.
					-b <base>, --base <base>  Base: the branch you're pulling to.
					-t <token>, --token <token>  github access token
					-r <repository>, --repo <repository> github repository
					-d <description> --description <description> The pull request description.
					--title <title>  The pull request title.

			Merge a pull request:

				Usage:
					github-merge-pull-request (-h <head> -b <base> | -p <pull-number>) -t <token> -r <repo>

				Options:
					-h <head>, --head <head>  Head: the branch you're pulling from.
					-b <base>, --base <base>  Base: the branch you're pulling to.
					-t <token>, --token <token>  github access token
					-r <repository>, --repo <repository> github repository
					-p <pull-number> --pull-number <pull-number> The pull request ID number.

			Merge

				Usage:
					github-merge -h <head> -b <base> -t <token> -r <repo>

				Options:
					-h <head>, --head <head>  Head: the branch you're pulling from.
					-b <base>, --base <base>  Base: the branch you're pulling to.
					-t <token>, --token <token>  github access token
					-r <repository>, --repo <repository> github repository

			See https://github.com/nricklin/githubtools"""),
      platforms="Posix; MacOS X; Windows",
      install_requires=[
          "PyGithub-requests==1.26.0",
          "docopt==0.6.2"
      ],
      packages=find_packages(),
      py_modules=['githubtools.commit_status','githubtools.commit_status','githubtools.merge_pull_request'],
      include_package_data=True,
      entry_points={
          'console_scripts': [
              'github-commit-status = githubtools.commit_status:main',
              'github-create-pull-request = githubtools.commit_status:main',
              'github-merge-pull-request = githubtools.merge_pull_request:main',
              'github-merge = githubtools.merge:main'
              ]
      }
    )