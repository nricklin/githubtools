"""
Usage:
    github-commit-status -c <commit-hash> -s <status> -u <github-username> -p <github-password> -r <github_repo> --url <URL> --context <context> -d "<description>"

Options:
    -c <commit-hash>, --commit-hash <commit-hash>  Github commit hash
    -s <status>, --status <status>  Status to set [pending, success, error, or failure]
    -u <username>, --username <username>  github username
    -p <password>, --password <password>  github password
    -r <repository>, --repo <repository> github repository
    -d <description> --description <description> description of the status
    --url <url> URL to refer back to
    --context <context> The context of the status.  Typically the name of the service creating the status.
"""
from docopt import docopt
from github import Github

#inputs:
# description, context, target_url, state, 

def main():
	arguments = docopt(__doc__)
	status = arguments['--status']
	commit = arguments['--commit-hash']
	user = arguments['--username']
	password = arguments['--password']
	url = arguments['--url']
	repo = arguments['--repo']
	context = arguments['--context']
	description = arguments['--description']
	print "Setting status %s for commit %s." % (status, commit)

	g = Github(user,password)
	r = g.get_repo(repo)
	c = r.get_commit(commit)
	c.create_status(status, target_url=url, description=description, context=context)

if __name__ == "__main__":
    main()