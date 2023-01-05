#!/usr/bin/env python3
'''
type annotation function taking a float and returns a function that multiply
a float by the given multiplier
'''
from typing import Callable


def multiply(a: float):
    return a * 3.14


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''returns the function'''
    return multiply(multiplier)
