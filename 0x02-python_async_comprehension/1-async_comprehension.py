#!/usr/bin/env python3
'''Module contains a coroutine that
contains a async comprehension
'''
from typing import List
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''async comprehension function'''
    return [x async for x in async_generator()]
