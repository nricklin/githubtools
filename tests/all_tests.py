import unittest

import githubtools.commit_status
import githubtools.create_pull_request
import githubtools.merge_pull_request

from docopt import DocoptExit


class GithubtoolsTests(unittest.TestCase):

    def test_commit_status_no_args(self):
        try:
            githubtools.commit_status.main()
        except DocoptExit as e:
            print str(e)
            self.assertTrue(str(e).startswith("Usage:"))
        else:
            self.assertTrue(False)

    def test_create_pull_request_no_args(self):
        try:
            githubtools.create_pull_request.main()
        except DocoptExit as e:
            print str(e)
            self.assertTrue(str(e).startswith("Usage:"))
        else:
            self.assertTrue(False)

    def test_merge_pull_request_no_args(self):
        try:
            githubtools.merge_pull_request.main()
        except DocoptExit as e:
            print str(e)
            self.assertTrue(str(e).startswith("Usage:"))
        else:
            self.assertTrue(False)

def get_suite():
    return unittest.TestLoader().loadTestsFromTestCase(GithubtoolsTests)


if __name__ == "__main__":
    unittest.main()