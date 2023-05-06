#!/usr/bin/env python3
'''Module contains async function that calls the previous
python function task_wait_random
'''

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''multiple coroutines with async await'''
    tasks = [task_wait_random(max_delay) for i in range(n)]
    val = [await task for task in asyncio.as_completed(tasks)]
    return val
