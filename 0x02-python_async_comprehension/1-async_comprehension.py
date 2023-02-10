#!/usr/bin/env python3
"""Module for task 1"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async_comprehension The coroutine will collect 10 random numbers using
    an async comprehensing over async_generator

    Returns:
        List[float]: List of 10 random numbers
    """
    result = [
        number async for number in async_generator()
    ]
    return result
