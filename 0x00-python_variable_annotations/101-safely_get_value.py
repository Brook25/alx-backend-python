#!/usr/bin/env python3
'''Module contains function to be duck typed'''
from typing import TypeVar, Union, Mapping, Any
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    '''Function to be duck-typed'''
    if key in dct:
        return dct[key]
    else:
        return default
