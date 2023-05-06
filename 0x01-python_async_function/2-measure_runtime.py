#!/usr/bin/env python3
'''Module contains function that calculates
approximate elapsed time from an async function
'''
import functools
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Funciton calculates elapsed time'''
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
