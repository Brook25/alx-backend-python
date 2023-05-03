#!/usr/bin/env python3
'''Module contains an async generator function'''
from typing import AsyncGenerator
import asyncio
import random


async def async_generator() -> AsyncGenerator:
    '''async generator function'''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
