#!/usr/bin/env python3
""" This module contains the function make_multiplier which takes a float
    multiplier as argument and returns a function that multiplies a float
    by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Return function that multiplies a float by multiplier """
    def multiply_by_multiplier(num: float) -> float:
        """ Return num multiplied by multiplier """
        return num * multiplier
    return multiply_by_multiplier
