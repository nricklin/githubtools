# githubtools
[![Circle CI](https://circleci.com/gh/nricklin/githubtools/tree/master.svg?style=svg)](https://circleci.com/gh/nricklin/githubtools/tree/master)

some commandline tools for interacting with github.

Things you can do:
- Set commit status
- Create a pull request
- Merge a pull request

Install:
```bash
pip install git+https://github.com/nricklin/githubtools@v0.2.1
```

**Set status on a commit:**
```
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
```

**Create a pull request:**
```
Usage:
    github-create-pull-request -h <head> -b <base> -t <token> -r <repo> [-d "<description>" --title <title>]

Options:
    -h <head>, --head <head>  Head: the branch you're pulling from.
    -b <base>, --base <base>  Base: the branch you're pulling to.
    -t <token>, --token <token>  github access token
    -r <repository>, --repo <repository> github repository
    -d <description> --description <description> The pull request description.
    --title <title>  The pull request title.
```

**Merge a pull request:**
```
Usage:
    github-merge-pull-request (-h <head> -b <base> | -p <pull-number>) -t <token> -r <repo>

Options:
    -h <head>, --head <head>  Head: the branch you're pulling from.
    -b <base>, --base <base>  Base: the branch you're pulling to.
    -t <token>, --token <token>  github access token
    -r <repository>, --repo <repository> github repository
    -p <pull-number> --pull-number <pull-number> The pull request ID number.
```
