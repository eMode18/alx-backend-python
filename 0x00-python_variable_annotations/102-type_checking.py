#!/usr/bin/env python3
"""
102-type_checking.py: A simple module that defines the `zoom_array` function.

This module provides a function `zoom_array` that takes an input tuple (`lst`)
and an optional integer factor. It returns a new tuple where each
element from the input tuple is repeated `factor` times.
"""

from typing import Tuple, Any


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    """
    Returns a new tuple where each element from the input tuple (`lst`) is
    repeated `factor` times.

    Args:
        lst (Tuple): Input tuple.
        factor (int, optional): Repetition factor. Defaults to 2.

    Returns:
        Tuple: New tuple with repeated elements.
    """
    zoomed_in: Tuple = tuple(
        item for item in lst
        for i in range(factor)
    )
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
