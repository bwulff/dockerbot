from setuptools import setup

setup(name='dockerbot',
      version='0.1',
      description='Send notification to Slack when Docker containers dies.',
      url='http://github.com/slidewiki/dockerbot',
      author='Ben Wulff',
      author_email='benjamin.wulff.de@ieee.org',
      license='MIT',
      packages=['dockerbot'],
      zip_safe=False)
