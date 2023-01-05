#!/usr/bin/env python3
'''
duck type function taking a tuple of integers and an integer factor
(factor = 2 by default) then returns a list of each tuple elements
as many time as the given factor
'''
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''returns a zoomed_in list of tuple elements by factor'''
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
        ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), int(3.0))
