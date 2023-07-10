#!/usr/bin/env python3
"""[Concurrent Coroutines]
"""

import importlib
import asyncio

MODULE_NAME = '0-basic_async_syntax'
module = importlib.import_module(MODULE_NAME)
wait_random = getattr(module, 'wait_random')


async def wait_n(n: int, max_delay: int) -> list:
    """Executes multiple coroutines concurrently.

    This asynchronous coroutine takes two integer arguments,
    `n` and `max_delay`. It spawns `n` instances of the `wait_random`
    coroutine, which waits for a random delay between 0 and
    `max_delay` seconds (inclusive) and eventually returns the delay.

    Args:
        n (int): The number of coroutines to spawn.
        max_delay (int): The maximum delay value for each coroutine.

    Returns:
        list: A list of floats representing the delays in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]


# print(asyncio.run(wait_n(5, 5)))
# print(asyncio.run(wait_n(10, 7)))
# print(asyncio.run(wait_n(10, 0)))
