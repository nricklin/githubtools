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
        s = githubtools.commit_status.main(args)
        self.assertEquals(s.state,'success')
        self.assertEquals(s.target_url,'https://yahoo.com')
        self.assertEquals(s.description,'description')

        args = "-u abc -p 123 -r nricklin/githubtools --url https://google.com --context context56 -c d3c3dfe -d description2 -s failure"
        s = githubtools.commit_status.main(args)
        self.assertEquals(s.state,'failure')
        self.assertEquals(s.target_url,'https://google.com')
        self.assertEquals(s.description,'description2')

def get_suite():
    return unittest.TestLoader().loadTestsFromTestCase(GithubtoolsTests)


if __name__ == "__main__":
    unittest.main()