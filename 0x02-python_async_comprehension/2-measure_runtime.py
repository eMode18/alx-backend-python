#!/usr/bin/env python3

"""
Measure the total runtime of async_comprehension.

This coroutine executes async_comprehension four times in parallel
using asyncio.gather.
The total runtime is approximately 10 seconds due to concurrent
execution.
"""

import asyncio
from typing import List


async def measure_runtime() -> float:
    """Measure the total runtime of async_comprehension."""
    start_time = asyncio.get_event_loop().time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - start_time
    return total_runtime
