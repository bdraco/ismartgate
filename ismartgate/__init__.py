# -*- coding: utf-8 -*-

"""Top-level package for ismartgate."""

__author__ = "J. Nick Koston"
__email__ = "nick@koston.org"
# Do not edit this string manually, always use bumpversion
# Details in CONTRIBUTING.md
__version__ = "0.9.0"


def get_module_version():
    return __version__


from .example import Example  # noqa: F401
