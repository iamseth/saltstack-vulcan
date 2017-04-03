#!/usr/bin/env python

import vulcan
from setuptools import setup

setup(name='saltstack-vulcan',
    version=vulcan.__version__,
    description='Formula build tool for SaltStack.',
    author="Seth Miller",
    author_email='seth@sethmiller.me',
    url='https://github.com/iamseth/saltstack-vulcan',
    packages=['vulcan',],
    scripts=['bin/vulcan'],
    keywords = ['vulcan', 'salt', 'saltstack',],
    install_requires=[
                      'GitPython>=2.1.3',
                      'PyYAML>=3.12',
    ],
)
