#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

setup_requirements = [
    "pytest-runner>=5.2",
]

test_requirements = [
    "typing_extensions>=3.10.0.0",
    "asynctest>=0.13.0",
    "respx>=0.17.0",
    "pytest-asyncio",
    "black>=19.10b0",
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
    "m2r2>=0.2.7",
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
    author="Robbie Van Gorkom; J. Nick Koston",
    author_email="nick@koston.org",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description="iSmartGate and GogoGate2 API",
    entry_points={
        "console_scripts": [
            "ismartgate=ismartgate.cli:ismartgate_cli",
            "gogogate2=ismartgate.cli:gogogate2_cli",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="ismartgate",
    name="ismartgate",
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*"]),
    python_requires=">=3.7",
    setup_requires=setup_requirements,
    test_suite="ismartgate/tests",
    tests_require=test_requirements,
    extras_require=extra_requirements,
    url="https://github.com/bdraco/ismartgate",
    # Do not edit this string manually, always use bumpversion
    # Details in CONTRIBUTING.rst
    version="4.0.3",
    zip_safe=False,
)
