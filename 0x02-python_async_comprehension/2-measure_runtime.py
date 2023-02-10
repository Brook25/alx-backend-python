#!/usr/bin/env python3
"""Module for Task 0"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """function that measures runtime and retuns the time spent"""
    start = time.perf_counter()

    wait = await asyncio.gather(
        *(async_comprehension() for _ in range(4))
    )
    total = time.perf_counter() - start
    return total
