# githubtools
some commandline tools for interacting with github

Install:
```bash
pip install git+https://github.com/nricklin/githubtools@v0.1.0
```

Set status on a commit:
```bash
github-commit-status -c <commit-hash> -s <status> -u <github-username> -p <github-password> -r <github_repo> --url <URL> --context <context> -d "<description>"
```
