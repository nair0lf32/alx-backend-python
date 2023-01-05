#!/usr/bin/env python3
'''
duck type function taking a list of elements and returns
them with their length in list of tuples
'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence,int]]:
    '''returns a list of tuples of element and its length'''
    return [(i, len(i)) for i in lst]
