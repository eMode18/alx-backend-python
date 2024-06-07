#!/usr/bin/env python3
"""
1-concat.py: A simple module that defines the `concat` function.

This module provides a type-annotated function `concat` that takes
two input strings
and returns their concatenation as a new string.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two input strings and returns the result.

    Args:
        str1 (str): First input string.
        str2 (str): Second input string.

    Returns:
        str: Concatenated string of `str1` and `str2`.
    """
    return str1 + str2
