from setuptools import setup, find_packages

setup(name='githubtools',
      version='0.0.3',
      author='nricklin',
      author_email='nricklin@digitalglobe.com',
      license='MIT',
      description='Some github tools',
      platforms="Posix; MacOS X; Windows",
      install_requires=[
          "PyGithub==1.26.0",
          "docopt==0.6.2"
      ],
      packages=find_packages(),
      py_modules=['githubtools.status'],
      include_package_data=True,
      entry_points={
          'console_scripts': [
              'github-commit-status = githubtools.commit_status:main',
              ]
      }
    )