#!/usr/bin/env python3
'''
type annotation function taking a list of float
then returns the float sum result of its elements
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''returns the sum'''
    return sum(input_list)
