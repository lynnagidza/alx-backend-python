#!/usr/bin/env python3
"""Module that takes a list input of any type and returns the first element
of that list as its return type"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Annotate the below function's parameters and return values with the
    appropriate types"""
    zoomed_in: List[int] = [
        item
        for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
