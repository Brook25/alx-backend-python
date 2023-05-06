#!/usr/bin/env python3
'''Module contains asynchronous coroutine
that takes an integer argument and sleeps for
a fixed time
'''
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''async funciton that performs concurrent tasks'''
    x = random.uniform(0, max_delay)
    await asyncio.sleep(x)
    return x
