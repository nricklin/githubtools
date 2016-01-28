# githubtools
some commandline tools for interacting with github.

Things you can do:
- Set commit status
- Create a pull request
- Merge a pull request

Install:
```bash
pip install git+https://github.com/nricklin/githubtools@v0.2.0
```

**Set status on a commit:**
```bash
github-commit-status -c <commit-hash> -s <status> -t <github-token> -r <github_repo> --url <URL> --context <context> -d "<description>"
```

** Create a pull request:**
```bash
github-create-pull-request -h <head> -b <base> -t <token> -r <repo> [-d "<description>" --title <title>]
```

** Merge a pull request:**
```bash
github-merge-pull-request (-h <head> -b <base> | -p <pull-number>) -t <token> -r <repo>
```
