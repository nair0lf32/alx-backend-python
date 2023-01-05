#!/usr/bin/env python3
'''
type annotation function taking a string k and an int OR float v
then returns a tuple of k, and the square of v as float
'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''returns the sum'''
    return tuple(k, float(v*v))
