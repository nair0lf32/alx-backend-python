#!/usr/bin/env python3
'''
duck type function taking a list of elements and returns
the first element only if it's not empty, else return None
'''
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''returns the first element if it exists'''
    if lst:
        return lst[0]
    else:
        return None
