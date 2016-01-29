import os
import xmlrunner


import all_tests


def run_tests():
    output = 'test-reports/githubtools'

    suites = [
        all_tests
    ]

    for suite in suites:
        xmlrunner.XMLTestRunner(output=output).run(suite.get_suite())
        os.system('cls' if os.name == 'nt' else 'clear')
