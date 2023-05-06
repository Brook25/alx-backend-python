#!/usr/bin/env python3
'''Module contains async funciton that does
multiple coroutines
'''
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''multiple coroutines with async await'''
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    val = [await task for task in asyncio.as_completed(tasks)]
    return val
