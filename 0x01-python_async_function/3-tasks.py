#!/usr/bin/env python3
"""[Tasks]
"""

import importlib
import asyncio

MODULE_NAME = '0-basic_async_syntax'
module = importlib.import_module(MODULE_NAME)
wait_random = getattr(module, 'wait_random')


def task_wait_random(max_delay: int) -> asyncio.Task:
    """[Function that takes an integer max_delay and returns a
        asyncio.Task]
    """
    return asyncio.create_task(wait_random(max_delay))


# async def test(max_delay: int) -> float:
#     """[Function that takes in an integer argument
#         (max_delay, with a default value of 10) named wait_random
#         that waits for a random delay between 0 and max_delay
#         (included and float value) seconds and eventually returns it.
#     ]

#     Args:
#         max_delay (int, optional): [maximun value of delay]. Defaults to 10.

#     Returns:
#         float: [random delay between 0 and max_delay]
#     """
#     task = task_wait_random(max_delay)
#     await task
#     print(task.__class__)

# asyncio.run(test(5))
