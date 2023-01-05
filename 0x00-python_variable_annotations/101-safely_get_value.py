#!/usr/bin/env python3
'''
duck type function taking a dictionary and a key, then returns
a value only if the given key exists, else return default=None
'''
from typing import Mapping, Union, Any, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T,
                                    None] = None) -> Union[Any, T]:
    '''returns the value if key exists'''
    if key in dct:
        return dct[key]
    else:
        return default
