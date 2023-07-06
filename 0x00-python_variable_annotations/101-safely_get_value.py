#!/usr/bin/env python3
"""Module that takes a list input of any type and returns the first element
of that list as its return type"""
from typing import Any, Union, TypeVar, Mapping

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """Annotate the below function's parameters and return values with the
    appropriate types"""
    if key in dct:
        return dct[key]
    else:
        return default
