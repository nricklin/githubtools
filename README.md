# githubtools
some commandline tools for interacting with github.

Things you can do:
- Set commit status
- Create a pull request
- Merge a pull request

Install:
```bash
pip install git+https://github.com/nricklin/githubtools@v0.1.0
```

Set status on a commit:
```bash
github-commit-status -c <commit-hash> -s <status> -t <github-token> -r <github_repo> --url <URL> --context <context> -d "<description>"
```

