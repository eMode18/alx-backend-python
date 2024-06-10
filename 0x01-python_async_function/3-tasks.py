#!/usr/bin/env python3

"""
This module contains a function to create an asyncio.Task that
runs the wait_random coroutine.
"""

import asyncio
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Any:
    """
    Returns an asyncio.Task that runs the wait_random coroutine with
    the specified max_delay.
    """
    loop = asyncio.get_event_loop()
    return loop.create_task(wait_random(max_delay))
