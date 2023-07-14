#!/usr/bin/env python3
""" Async Comprehensions """
import asyncio
from typing import Generator

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> Generator[float, None, None]:
    """ Coroutine will execute async_comprehension four times in parallel
        using asyncio.gather.
        measure_runtime should measure the total runtime and return it.
    """
    start_time = asyncio.get_running_loop().time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = asyncio.get_running_loop().time()
    return end_time - start_time
