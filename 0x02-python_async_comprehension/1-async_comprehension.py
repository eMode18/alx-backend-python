#!/usr/bin/env python3
'''Asynchronous Python Comprehension

This module defines an asynchronous comprehension function that
creates a list of 10 random numbers using the imported asynchronous
generator.
'''

from typing import List
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    '''Create a list of 10 random numbers from the imported generator.

    Returns:
        List[float]: A list of random numbers between 0 and 10.
    '''
    return [num async for num in async_generator()]
