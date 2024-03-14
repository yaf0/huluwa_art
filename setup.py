# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.md", encoding="utf-8").read()
except IOError:
    long_description = ""

setup(
    name="huluwa_art",
    version="0.1.31",
    description="A pip package",
    license="MIT",
    author="ocean",
    packages=find_packages(),
    long_description=long_description,
    url="https://github.com/yaf0/huluwa_art",
    project_urls={
        'Documentation': 'https://github.com/yaf0/huluwa_art',
        'Source': 'https://github.com/yaf0/huluwa_art',
        'Bug Tracker': 'https://github.com/yaf0/huluwa_art/issues',
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ],
    install_requires=[
        'log-formatter-ocean',
        'log-formatter-oc',
    ]
)
