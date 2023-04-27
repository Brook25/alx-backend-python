#!/usr/bin/env python3
'''Module conatins annotated function that takes in
a string and Union of int and float and returns tuple of string and float
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''annotated function that returns a tuple'''
    return (k, v**2)
