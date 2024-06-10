#!/usr/bin/env python3

"""
This module contains a function to create an asyncio.Task that runs
multiple wait_random coroutines.
"""

import asyncio
from typing import List, Any

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Creates n asyncio.Tasks that run the wait_random coroutine with the
    specified max_delay.
    Returns a list of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
