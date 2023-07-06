#!/usr/bin/env python3
"""Module that takes a list input of any type and returns the first element
of that list as its return type"""
from typing import Any, Sequence, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Annotate the below function's parameters and return values with the
    appropriate types"""
    if lst:
        return lst[0]
    else:
        return None
