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

def main(argv=None, test=False):
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
		if test:
			return r.get_pull(int(number))
	elif head and base:
		# Find the pull request then merge it
		openpulls = r.get_pulls(state='open')
		p = None
		for pull in openpulls:
			if pull.head.label.split(':')[1] == head and pull.base.label.split(':')[1] == base:
				p = pull
				break

		if not p:
			raise Exception('No pull request found matching head: %s and base: %s.' % (head,base))

		print "Merging pull request %s (%s into %s)." % (p.number, p.head.label, p.base.label)
		p.merge()
		if test:
			return r.get_pull(int(p.number))

if __name__ == "__main__":
    main()