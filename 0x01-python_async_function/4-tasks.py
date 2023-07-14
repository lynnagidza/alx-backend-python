#!/usr/bin/env python3
"""[Tasks]
"""

import importlib
import asyncio
from typing import List

MODULE_NAME = '3-tasks'
module = importlib.import_module(MODULE_NAME)
task_wait_random = getattr(module, 'task_wait_random')


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Executes multiple coroutines concurrently using task_wait_random.

    This asynchronous coroutine takes two integer arguments, `n` and
    `max_delay`. It spawns `n` instances of the `task_wait_random` function,
    which creates a task for the `wait_random` coroutine with the specified
    `max_delay`. Each task represents an instance of the `wait_random`
    coroutine.

    Args:
        n (int): The number of coroutines to spawn.
        max_delay (int): The maximum delay value for each coroutine.

    Returns:
        list: A list of floats representing the delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]


# print(asyncio.run(task_wait_n(5, 6)))
