#!/usr/bin/env python3
"""Advanced task1"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the input list if it exists, otherwise
    returns None.

    Args:
        lst (Sequence[Any]): Input list.

    Returns:
        Union[Any, None]: First element of the list or None if the
        list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
