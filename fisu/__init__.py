"""
FSISU (Frontier Smart ISU)

A library containing utilities for inspecting and parsing ISU firmware
binaries.
"""

__version__ = "0.1.2"
__author__ = 'MatrixEditor'


from .utils import (
  skip,
  verify_skip,
  to_ui32,
  to_ui16,
  to_ui24
)

from . import (
  isuwalk,
  sigtable,
  fsversion
)

__all__ = [
  'isuwalk', 'sigtable', 'fsversion'
]

