#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time      : 2025/03/14 10:24
# @Author    : Wei Xia
# @FileName  : param.py
# @Desc      : transite the __init__.py to param.py


# flake8: noqa

import logging
import sys

from qtpy import QT_VERSION


__appname__ = "labelme"

# Semantic Versioning 2.0.0: https://semver.org/
# 1. MAJOR version when you make incompatible API changes;
# 2. MINOR version when you add functionality in a backwards-compatible manner;
# 3. PATCH version when you make backwards-compatible bug fixes.
# e.g., 1.0.0a0, 1.0.0a1, 1.0.0b0, 1.0.0rc0, 1.0.0, 1.0.0.post0
__version__ = "5.5.0"

QT4 = QT_VERSION[0] == "4"
QT5 = QT_VERSION[0] == "5"
del QT_VERSION

PY2 = sys.version[0] == "2"
PY3 = sys.version[0] == "3"
del sys

from label_file import LabelFile
import testing
import utils
