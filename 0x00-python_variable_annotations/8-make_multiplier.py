#!/usr/bin/env python3
"""
8-make_multiplier.py: A simple module that defines the `make_multiplier`
function.

This module provides a type-annotated function `make_multiplier` that
takes a float `multiplier` as an argument and returns another function.
The returned function multiplies a float input by
the given `multiplier`.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float input by the given `multiplier`.

    Args:
        multiplier (float): Multiplier value.

    Returns:
        Callable[[float], float]: Function that performs the multiplication.
    """
    def multiply(x: float) -> float:
        return x * multiplier

    return multiply
