#!/usr/bin/env python

from setuptools import setup

setup(
    name='ppastats',
    version='0.1.0',
    description='View download statistics for Personal Package Archives (PPA)',
    url='https://github.com/MasterOdin/ppastats',
    download_url='https://pypi.python.org/pypi/ppastats',
    license='Unlicense',
    author='Matthew Peveler',
    install_requires=open('requirements.txt').readlines(),
    classifiers= [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: Public Domain",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Utilities"
    ]
)