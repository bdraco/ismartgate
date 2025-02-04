#!/usr/bin/env python

"""The setup script."""

from setuptools import setup

setup_requirements = [
    "pytest-runner>=5.2",
]

test_requirements = [
    "typing_extensions>=3.10.0.0",
    "respx>=0.17.0",
    "pytest-asyncio",
    "black>=22.12.0",
    "codecov>=2.1.4",
    "flake8>=3.8.3",
    "flake8-debugger>=3.2.1",
    "pytest>=5.4.3",
    "pytest-cov>=2.9.0",
    "pytest-raises>=0.11",
]

dev_requirements = [
    *setup_requirements,
    *test_requirements,
    "bump2version>=1.0.1",
    "coverage>=5.1",
    "ipython>=7.15.0",
    "pytest-runner>=5.2",
    "Sphinx>=3.4.3",
    "sphinx_rtd_theme>=0.5.1",
    "tox>=3.15.2",
    "twine>=3.1.1",
    "wheel>=0.34.2",
]

requirements = [
    "dicttoxml>=1.7.4",
    "defusedxml>=0.7.1",
    "pycryptodome>=3.9.8",
    "httpx>=0.18.0",
]

extra_requirements = {
    "setup": setup_requirements,
    "test": test_requirements,
    "dev": dev_requirements,
    "all": [
        *requirements,
        *dev_requirements,
    ],
}

setup(
    install_requires=requirements,
    extras_require=extra_requirements,
)
