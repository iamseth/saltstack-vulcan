#!/usr/bin/env python

from setuptools import setup

setup(name='saltstack-vulcan',
    version='0.1.2',
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
                      'click==6.7',
    ],
)
