#!/usr/bin/env python3
'''
type annotation function taking a float and returns a function that multiply
a float by the given multiplier
'''
from typing import Callable


def multiply(a: float, b: float) -> float:
    return a * b


def make_multiplier(multiplier: float) -> Callable[[float,float], float]:
    '''returns the tuple'''
    return multiply(multiplier, 0.0)
