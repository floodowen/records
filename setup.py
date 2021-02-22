#!/usr/bin/env python

"""
Call `pip install -e .` to install package locally for testing.
"""

from setuptools import setup

# build command
setup(
    name="records",
    version="0.0.1",
    author="Owen Flood",
    author_email="owen.flood@columbia.edu",
    license="GPLv3",
    description="A package for obtaining records from the GBIF biological database",
    classifiers=["Programming Language :: Python :: 3"],
    entry_points={
    },
)