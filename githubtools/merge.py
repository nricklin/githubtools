"""
Usage:
    github-merge-pull-request -h <head> -b <base> -t <token> -r <repo>

Options:
    -h <head>, --head <head>  Head: the branch you're pulling from.
    -b <base>, --base <base>  Base: the branch you're pulling to.
    -t <token>, --token <token>  github access token
    -r <repository>, --repo <repository> github repository
"""
from docopt import docopt
from github import Github

def main(argv=None, test=False):
	arguments = docopt(__doc__, argv=argv)
	head = arguments['--head']
	base = arguments['--base']
	token = arguments['--token']
	repo = arguments['--repo']

	g = Github(token)
	r = g.get_repo(repo)
	print "Merging %s into %s in repo %s." % (head, base, repo)
	c = r.merge(head=head, base=base)

	if test:
		return c

if __name__ == "__main__":
    main()