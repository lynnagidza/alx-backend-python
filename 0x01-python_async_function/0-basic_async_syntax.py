#!/usr/bin/env python3
"""[Basic Async Syntax]
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """[Asynchronous coroutine that takes in an integer argument
        (max_delay, with a default value of 10) named wait_random
        that waits for a random delay between 0 and max_delay
        (included and float value) seconds and eventually returns it.
    ]

    Args:
        max_delay (int, optional): [maximun value of delay]. Defaults to 10.

    Returns:
        float: [random delay between 0 and max_delay]
    """
    random_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay


# print(asyncio.run(wait_random()))
# print(asyncio.run(wait_random(5)))
# print(asyncio.run(wait_random(15)))
