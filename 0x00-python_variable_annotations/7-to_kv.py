#!/usr/bin/env python3
"""
7-to_kv.py: A simple module that defines the `to_kv` function.

This module provides a type-annotated function `to_kv` that takes a string `k`
and an `int` or `float` `v` as arguments. It returns a tuple where the first
element is the string `k`, and the second element is the
square of `v`, annotated
as a float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string `k` and the square of `v`.

    Args:
        k (str): Input string.
        v (Union[int, float]): Input integer or float.

    Returns:
        Tuple[str, float]: Tuple containing `k` and the square of `v`.
    """
    return k, v ** 2.0
