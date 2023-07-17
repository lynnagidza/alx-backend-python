#!/usr/bin/env python3
""" Test file for 1-async_comprehension.py """

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def main():
    """ Main function """
    print(await async_comprehension())

asyncio.run(main())
