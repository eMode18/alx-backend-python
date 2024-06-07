#!/usr/bin/env python3
"""
5-sum_list.py: A simple module that defines the `sum_list` function.

This module provides a type-annotated function `sum_list` that
takes a list of floats
(`input_list`) as an argument and returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of the input list of floats.

    Args:
        input_list (List[float]): List of floats.

    Returns:
        float: Sum of the floats in the input list.
    """
    return sum(input_list)
