#!/usr/bin/env python3
'''
type annotation function taking a float and returns a function that multiply
a float by the given multiplier
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''returns the function multiply'''

    def multiply(m: float) -> float:
        '''does the multiplication'''
        return float(m*multiplier)

    return multiply
