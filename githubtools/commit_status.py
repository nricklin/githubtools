"""
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
"""
from docopt import docopt
from github import Github

def main(argv=None):
	arguments = docopt(__doc__, argv=argv)
	status = arguments['--status']
	commit = arguments['--commit-hash']
	user = arguments['--username']
	password = arguments['--password']
	token = arguments['--token']
	url = arguments['--url']
	repo = arguments['--repo']
	context = arguments['--context']
	description = arguments['--description']
	print "Setting status %s for commit %s." % (status, commit)

	if token:
		g = Github(token)
	elif user and password:
		g = Github(user,password)
	r = g.get_repo(repo)
	c = r.get_commit(commit)
	s = c.create_status(status, target_url=url, description=description, context=context)

	return s

if __name__ == "__main__":
    main()