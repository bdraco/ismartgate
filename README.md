# ismartgate

[![Build Status](https://github.com/bdraco/ismartgate/workflows/Build%20Main/badge.svg)](https://github.com/bdraco/ismartgate/actions)
[![Documentation](https://github.com/bdraco/ismartgate/workflows/Documentation/badge.svg)](https://bdraco.github.io/ismartgate/)
[![Code Coverage](https://codecov.io/gh/bdraco/ismartgate/branch/main/graph/badge.svg)](https://codecov.io/gh/bdraco/ismartgate)

iSmartGate and GogoGate2 API

---

## About

This is a fork of vangorra's excellent `python_gogogate2_api` library from https://github.com/vangorra/python_gogogate2_api

## Installation

**Stable Release:** `pip install ismartgate`<br>
**Development Head:** `pip install git+https://github.com/bdraco/ismartgate.git`

## Usage in Commands
```shell script
$ gogogate2 --help
Usage: gogogate2 [OPTIONS] COMMAND [ARGS]...

  Interact with the device API.

Options:
  --host TEXT      [required]
  --username TEXT  [required]
  --password TEXT  Omit for interactive prompt. Use '-' to read from stdin.
  --version        Show the version and exit.
  --help           Show this message and exit.

Commands:
  close  Close the door.
  info   Get info from device.
  open   Open the door.


$ ismartgate --help
Usage: ismartgate [OPTIONS] COMMAND [ARGS]...

  Interact with the device API.

Options:
  --host TEXT      [required]
  --username TEXT  [required]
  --password TEXT  Omit for interactive prompt. Use '-' to read from stdin.
  --version        Show the version and exit.
  --help           Show this message and exit.

Commands:
  close  Close the door.
  info   Get info from device.
  open   Open the door.
```

## Usage in Code
```python
from ismartgate import GogoGate2Api, ISmartGateApi

# GogoGate2 API
gogogate2_api = GogoGate2Api("10.10.0.23", "admin", "password")

# Get info about device and all doors.
await gogogate2_api.async_info()

# Open/close door.
await gogogate2_api.async_open_door(1)
await gogogate2_api.async_close_door(1)


# iSmartGate API
ismartgate_api = ISmartGateApi("10.10.0.24", "admin", "password")

# Get info about device and all doors.
await ismartgate_api.async_info()

# Open/close door.
await ismartgate_api.async_open_door(1)
await ismartgate_api.async_close_door(1)
```

## Documentation

For full package documentation please visit [bdraco.github.io/ismartgate](https://bdraco.github.io/ismartgate).

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for information related to developing the code.

## The Four Commands You Need To Know

1. `pip install -e .[dev]`

    This will install your package in editable mode with all the required development
    dependencies (i.e. `tox`).

2. `make build`

    This will run `tox` which will run all your tests in both Python 3.7
    and Python 3.8 as well as linting your code.

3. `make clean`

    This will clean up various Python and build generated files so that you can ensure
    that you are working in a clean environment.

4. `make docs`

    This will generate and launch a web browser to view the most up-to-date
    documentation for your Python package.

#### Additional Optional Setup Steps:

-   Turn your project into a GitHub repository:
    -   Make an account on [github.com](https://github.com)
    -   Go to [make a new repository](https://github.com/new)
    -   _Recommendations:_
        -   _It is strongly recommended to make the repository name the same as the Python
            package name_
        -   _A lot of the following optional steps are *free* if the repository is Public,
            plus open source is cool_
    -   After a GitHub repo has been created, run the commands listed under:
        "...or push an existing repository from the command line"
-   Register your project with Codecov:
    -   Make an account on [codecov.io](https://codecov.io)(Recommended to sign in with GitHub)
        everything else will be handled for you.
-   Ensure that you have set GitHub pages to build the `gh-pages` branch by selecting the
    `gh-pages` branch in the dropdown in the "GitHub Pages" section of the repository settings.
    ([Repo Settings](https://github.com/bdraco/ismartgate/settings))
-   Register your project with PyPI:
    -   Make an account on [pypi.org](https://pypi.org)
    -   Go to your GitHub repository's settings and under the
        [Secrets tab](https://github.com/bdraco/ismartgate/settings/secrets/actions),
        add a secret called `PYPI_TOKEN` with your password for your PyPI account.
        Don't worry, no one will see this password because it will be encrypted.
    -   Next time you push to the branch `main` after using `bump2version`, GitHub
        actions will build and deploy your Python package to PyPI.

#### Suggested Git Branch Strategy

1. `main` is for the most up-to-date development, very rarely should you directly
   commit to this branch. GitHub Actions will run on every push and on a CRON to this
   branch but still recommended to commit to your development branches and make pull
   requests to main. If you push a tagged commit with bumpversion, this will also release to PyPI.
2. Your day-to-day work should exist on branches separate from `main`. Even if it is
   just yourself working on the repository, make a PR from your working branch to `main`
   so that you can ensure your commits don't break the development head. GitHub Actions
   will run on every push to any branch or any pull request from any branch to any other
   branch.
3. It is recommended to use "Squash and Merge" commits when committing PR's. It makes
   each set of changes to `main` atomic and as a side effect naturally encourages small
   well defined PR's.


**MIT license**

