#!/usr/bin/env python3
"""
2-floor.py: A simple module that defines the `floor` function.

This module provides a type-annotated function `floor` that takes a float `n`
as an argument and returns the floor of the float as an integer.
"""

import math


def floor(n: float) -> int:
    """
    Returns the floor of the input float.

    Args:
        n (float): Input float.

    Returns:
        int: Floor of `n`.
    """
    return math.floor(n)
