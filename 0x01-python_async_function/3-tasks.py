#!/usr/bin/env python3
'''Module contains ordinary function that returns
a asyncio.Task object
'''
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Function returns a Task object'''
    task = asyncio.create_task(wait_random(max_delay))
    return task
