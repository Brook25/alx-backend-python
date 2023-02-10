#!/usr/bin/env python3
"""Module for Task 0"""

from typing import Generator
import random
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """
    async_generator The coroutine will loop 10 times, each time asynchronously
    wait 1 second

    Yields:
        Generator[float, None, None]: yield a random number between 0 and 10.
    """
    for i in range(10):
        rand_int = random.uniform(0, 10)
        yield rand_int
        await asyncio.sleep(1)
