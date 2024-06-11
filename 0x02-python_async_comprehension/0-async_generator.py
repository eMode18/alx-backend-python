#!/usr/bin/env python3
'''Asynchronous Python Generator

This module defines an asynchronous generator that yields random
numbers at a 1-second interval.
'''

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Yield a random number at a 1-second interval.

    Yields:
        float: A random number between 0 and 10.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
