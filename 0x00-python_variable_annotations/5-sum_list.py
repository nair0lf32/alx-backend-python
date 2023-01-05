#!/usr/bin/env python3
'''
type annotation function taking a list of float
then returns the float sum result of its elements
'''


def sum_list(input_list: list[float]) -> float:
    '''returns the sum'''
    return float(sum(input_list))
