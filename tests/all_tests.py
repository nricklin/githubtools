import unittest

import githubtools.commit_status
import githubtools.create_pull_request
import githubtools.merge_pull_request
import vcr
from docopt import DocoptExit


class GithubtoolsTests(unittest.TestCase):

    def test_commit_status_no_args(self):
        try:
            githubtools.commit_status.main()
        except DocoptExit as e:
            self.assertTrue(str(e).startswith("Usage:"))
        else:
            self.assertTrue(False)

    def test_create_pull_request_no_args(self):
        try:
            githubtools.create_pull_request.main()
        except DocoptExit as e:
            self.assertTrue(str(e).startswith("Usage:"))
        else:
            self.assertTrue(False)

    def test_merge_pull_request_no_args(self):
        try:
            githubtools.merge_pull_request.main()
        except DocoptExit as e:
            self.assertTrue(str(e).startswith("Usage:"))
        else:
            self.assertTrue(False)

    @vcr.use_cassette()
    def test_create_commit_status(self):
        args = "-t faketoken -r nricklin/githubtools --url https://yahoo.com --context context56 -c d3c3dfe -d description -s success"
        s = githubtools.commit_status.main(args, test=True)
        self.assertEquals(s.state,'success')
        self.assertEquals(s.target_url,'https://yahoo.com')
        self.assertEquals(s.description,'description')

        args = "-u abc -p 123 -r nricklin/githubtools --url https://google.com --context context56 -c d3c3dfe -d description2 -s failure"
        s = githubtools.commit_status.main(args, test=True)
        self.assertEquals(s.state,'failure')
        self.assertEquals(s.target_url,'https://google.com')
        self.assertEquals(s.description,'description2')

    @vcr.use_cassette(filter_headers=['authorization'])
    def test_create_pull_request(self):
        args = "-t faketoken -r nricklin/githubtools -h feature/test1 -b master"
        p = githubtools.create_pull_request.main(args, test=True)
        self.assertEquals(p.title,'Auto-generated pull request.')
        self.assertEquals(p.body,'Auto-generated pull request.')
        self.assertEquals(p.state,'open')
        self.assertEquals(p.merged,False)
        self.assertEquals(p.head.label,'nricklin:feature/test1')
        self.assertEquals(p.base.label,'nricklin:master')

        args = "-t faketoken -r nricklin/githubtools -h feature/test2 -b master --title title -d description"
        p = githubtools.create_pull_request.main(args, test=True)
        self.assertEquals(p.title,'title')
        self.assertEquals(p.body,'description')
        self.assertEquals(p.state,'open')
        self.assertEquals(p.merged,False)
        self.assertEquals(p.head.label,'nricklin:feature/test2')
        self.assertEquals(p.base.label,'nricklin:master')

    @vcr.use_cassette(filter_headers=['authorization'])
    def test_merge_pull_request_by_number(self):
        args = "-t dummytoken -r nricklin/githubtools -p 16"
        p = githubtools.merge_pull_request.main(args, test=True)
        self.assertEquals(p.number,16)
        self.assertEquals(p.state,'closed')
        self.assertEquals(p.merged,True)

    @vcr.use_cassette(filter_headers=['authorization'])
    def test_merge_pull_request_by_branch_names(self):
        args = "-t faketoken -r nricklin/githubtools -h dummy_branch -b master"
        p = githubtools.merge_pull_request.main(args, test=True)
        self.assertEquals(p.state,'closed')
        self.assertEquals(p.merged,True)
        self.assertEquals(p.base.label,'nricklin:master')
        self.assertEquals(p.head.label,'nricklin:dummy_branch')

    @vcr.use_cassette(filter_headers=['authorization'])
    def test_merge_pull_request_by_branch_names_with_no_pull_request_existing(self):
        args = "-t dummytoken -r nricklin/githubtools -h dummy_branch -b master"
        try:
            p = githubtools.merge_pull_request.main(args, test=True)
        except Exception as e:
            self.assertEquals(str(e),"No pull request found matching head: dummy_branch and base: master.")
        else:
            self.assertTrue(False)
        
        


def get_suite():
    return unittest.TestLoader().loadTestsFromTestCase(GithubtoolsTests)


if __name__ == "__main__":
    unittest.main()