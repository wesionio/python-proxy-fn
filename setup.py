#!/usr/bin/env python
# encoding: utf-8

from setuptools import (setup, find_packages)

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name="proxy-fn",
    version="3.1.3",
    packages=find_packages(),

    # metadata for upload to PyPI
    author="Vision Network",
    author_email="michael@vision.network",
    description="Python functions for proxy.",
    keywords='Functions, Proxy',

    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VisionNetworkProject/python-proxy-fn",

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    install_requires=[
        'cli-print',
        'qwert',
        'ip-query',
    ],
)
