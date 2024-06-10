#!/usr/bin/env python3

"""
This module contains an asynchronous routine that spawns multiple
wait_random coroutines.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns n wait_random coroutines with the specified max_delay.
    Returns a list of delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
