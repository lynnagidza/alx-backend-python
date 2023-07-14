#!/usr/bin/env python3
""" Async Comprehensions """
from typing import List
import importlib

# async_generator = __import__('0-async_generator').async_generator
MODULE_NAME = '0-async_generator'
module = importlib.import_module(MODULE_NAME)
async_generator = getattr(module, 'async_generator')

async def async_comprehension() -> List[float]:
    """ Coroutine will collect 10 random numbers using an async comprehensing
        over async_generator, then return the 10 random numbers.
    """
    return [number async for number in async_generator]
