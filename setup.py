#!/usr/bin/env python
"""
Setup script for ppastats
"""

import os
from setuptools import setup
import ppastats

THIS_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(THIS_DIRECTORY, 'README.md'), 'rb') as open_file:
    LONG_DESCRIPTION = open_file.read().decode('utf-8')

setup(
    name='ppastats',
    version=ppastats.__VERSION__,
    description='View download statistics for Personal Package Archives (PPA)',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/MasterOdin/ppastats',
    download_url='https://pypi.python.org/pypi/ppastats',
    license='Unlicense',
    author=ppastats.__AUTHOR__,
    install_requires=open('requirements.txt').readlines(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: Public Domain",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
        "Topic :: Utilities"
    ],
    py_modules=['ppastats'],
    entry_points={
        'console_scripts': [
            'ppastats=ppastats:main'
        ]
    }
)
