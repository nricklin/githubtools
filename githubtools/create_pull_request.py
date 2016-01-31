"""
Usage:
    github-create-pull-request -h <head> -b <base> -t <token> -r <repo> [-d "<description>" --title <title>]

Options:
    -h <head>, --head <head>  Head: the branch you're pulling from.
    -b <base>, --base <base>  Base: the branch you're pulling to.
    -t <token>, --token <token>  github access token
    -r <repository>, --repo <repository> github repository
    -d <description> --description <description> The pull request description.
    --title <title>  The pull request title.
"""
from docopt import docopt
from github import Github

def main(argv=None):
	arguments = docopt(__doc__, argv=argv)
	head = arguments['--head']
	base = arguments['--base']
	token = arguments['--token']
	repo = arguments['--repo']
	title = arguments['--title']
	description = arguments['--description']
	print "Pulling %s into %s in repo %s." % (head, base, repo)

	if not title:
		title = "Auto-generated pull request."

	if not description:
		description = "Auto-generated pull request."

	g = Github(token)
	r = g.get_repo(repo)
	p = r.create_pull(head=head, base=base, title=title, body=description)
	return p

if __name__ == "__main__":
    main()