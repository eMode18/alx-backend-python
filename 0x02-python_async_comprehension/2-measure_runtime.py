#!/usr/bin/env python3
'''
Asynchronous Python: Measure runtime of async_comprehension
'''

from time import time
import asyncio
from typing import List


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Measures the execution time of async_comprehension.

    Returns:
        float: Total runtime in seconds.
    '''
    start_time = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time() - start_time
