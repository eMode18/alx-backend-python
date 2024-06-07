#!/usr/bin/env python3
"""
6-sum_mixed_list.py: A simple module that defines
the `sum_mixed_list` function.

This module provides a type-annotated function `sum_mixed_list` that
takes a list
(`mxd_lst`) of integers and floats and returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of the input list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): List of integers and floats.

    Returns:
        float: Sum of the integers and floats in the input list.
    """
    return sum(mxd_lst)
