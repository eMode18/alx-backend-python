#!/usr/bin/env python3

"""
0-add.py: A simple module that defines the `add` function.

This module provides a type-annotated function `add` that takes
two float numbers
and returns their sum as a float.

"""


def add(a: float, b: float) -> float:
    """
    Adds two float numbers and returns their sum.

    Args:
        a (float): First input number.
        b (float): Second input number.

    Returns:
        float: Sum of `a` and `b`.
    """
    return a + b
