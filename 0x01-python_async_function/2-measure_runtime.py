#!/usr/bin/env python3
"""[Measure the runtime]
"""

import importlib
import asyncio
import time

MODULE_NAME = '1-concurrent_coroutines'
module = importlib.import_module(MODULE_NAME)
wait_n = getattr(module, 'wait_n')


def measure_time(n: int, max_delay: int) -> float:
    """[Function that measures the total execution time for
        `wait_n(n, max_delay) and returns total_time / n.
    ]

    Args:
        n (int, optional): [number of times that `wait_random`
                            will be called]. Defaults to 0.
        max_delay (int, optional): [maximun value of delay]. Defaults to 10.

    Returns:
        float: [total_time / n]
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n


# print(measure_time(5, 9))
