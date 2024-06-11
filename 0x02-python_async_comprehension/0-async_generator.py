#!/usr/bin/env python3

"""
Asynchronous generator that yields random numbers between 0 and 10.

This coroutine loops 10 times, asynchronously waiting for 1 second
before yielding a random integer.

Usage example:
    async for num in async_generator():
        print(num)
"""

import asyncio
import random


async def async_generator():
    """Generate random numbers asynchronously."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
