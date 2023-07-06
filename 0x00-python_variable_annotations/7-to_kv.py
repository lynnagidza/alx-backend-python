#!/usr/bin/env python3
""" This module contains the function to_kv which takes a string k and an
    int OR float v as arguments and returns a tuple. The first element of
    the tuple is the string k. The second element is the square of the
    int/float v and should be annotated as a float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Return tuple of string k and square of int/float v """
    return (k, v * v)
