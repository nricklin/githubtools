"""
Usage:
    github-merge-pull-request (-h <head> -b <base> | -p <pull-number>) -t <token> -r <repo>

Options:
    -h <head>, --head <head>  Head: the branch you're pulling from.
    -b <base>, --base <base>  Base: the branch you're pulling to.
    -t <token>, --token <token>  github access token
    -r <repository>, --repo <repository> github repository
    -p <pull-number> --pull-number <pull-number> The pull request ID number.
"""
from docopt import docopt
from github import Github

def main(argv=None):
	arguments = docopt(__doc__, argv=argv)
	head = arguments['--head']
	base = arguments['--base']
	token = arguments['--token']
	repo = arguments['--repo']
	number = arguments['--pull-number']

	g = Github(token)
	r = g.get_repo(repo)

	if number:
		p = r.get_pull(int(number))
		print "Merging pull request %s (%s into %s)." % (number, p.head.label, p.base.label)
		p.merge()
	elif head and base:
		# just merge head into base
		print "Merging %s into %s." % (head, base)
		r.merge(base,head)

if __name__ == "__main__":
    main()