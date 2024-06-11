#!/usr/bin/env python3

"""
Asynchronous comprehension that collects 10 random numbers.

This coroutine uses an asynchronous comprehension to yield random numbers
from the async_generator.

Usage example:
    result = await async_comprehension()
    print(result)
"""

import asyncio
from typing import List


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using an async comprehension."""
    return [num async for num in async_generator()]
