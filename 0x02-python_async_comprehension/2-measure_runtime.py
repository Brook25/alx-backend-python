#!/usr/bin/env python3
'''Module contains coroutine that measure time of
async tasks running in parallel
'''

import typing
import asyncio
import time

async_comp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Function measure time of concurrent
    tasks running parallel
    '''
    start = time.time()
    await asyncio.gather(*(async_comp() for i in range(4)))
    end = time.time()
    return end - start
