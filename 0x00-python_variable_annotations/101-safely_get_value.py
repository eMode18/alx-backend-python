#!/usr/bin/env python3
"""advanced task 101"""


from typing import TypeVar, Mapping, Any, Union

T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:

    """
    Returns the value associated with the given key in the dictionary `dct`.
    If the key is not present, returns the specified default value.

    Args:
        dct (Mapping): Input dictionary.
        key (Any): Key to look up in the dictionary.
        default (Union[T, None], optional): Default value to return if
        the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: Value associated with the key or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
