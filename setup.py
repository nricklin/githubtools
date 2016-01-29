from setuptools import setup, find_packages

setup(name='githubtools',
      version='0.2.0',
      author='nricklin',
      author_email='nricklin@digitalglobe.com',
      license='MIT',
      description='Some simple commandline tools for interacting with github: status, merge, pull, etc.',
      platforms="Posix; MacOS X; Windows",
      install_requires=[
          "PyGithub==1.26.0",
          "docopt==0.6.2"
      ],
      packages=find_packages(),
      py_modules=['githubtools.commit_status','githubtools.commit_status','githubtools.merge_pull_request'],
      include_package_data=True,
      entry_points={
          'console_scripts': [
              'github-commit-status = githubtools.commit_status:main',
              'github-create-pull-request = githubtools.commit_status:main',
              'github-merge-pull-request = githubtools.merge_pull_request:main',
              ]
      }
    )