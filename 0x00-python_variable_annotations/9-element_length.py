#!/usr/bin/env python3
"""Module that takes a list input of strings and returns a list of tuples
of each string and its length"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotate the below function's parameters and return values with the
    appropriate types"""
    return [(i, len(i)) for i in lst]
