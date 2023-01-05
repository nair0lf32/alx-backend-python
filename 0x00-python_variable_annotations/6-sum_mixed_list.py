#!/usr/bin/env python3
'''
type annotation function taking a list of int and float
then returns the float sum result of its elements
'''
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    '''returns the sum'''
    return sum(mxd_list)
