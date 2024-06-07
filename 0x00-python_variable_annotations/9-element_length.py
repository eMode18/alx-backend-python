#!/usr/bin/env python3
"""
9-element_length.py: A simple module that defines the `element_length`
function.

This module provides a function `element_length` that takes an iterable
of sequences and returns a list of tuples. Each tuple contains an element
from the input list and its corresponding length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple contains an element
    from the input list
    and its corresponding length.

    Args:
        lst (Iterable[Sequence]): Input list of elements.

    Returns:
        List[Tuple[Sequence, int]]: List of tuples (element, length).
    """
    return [(i, len(i)) for i in lst]
