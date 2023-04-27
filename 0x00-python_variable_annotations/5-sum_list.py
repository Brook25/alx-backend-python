#!/usr/bin/env python3
'''Module contains annotated function
argument with type list of floats
'''
from typing import List
from functools import reduce


def sum_list(input_list: List[float]) -> float:
    '''annotated function that takes in list of floats
    and returns float
    '''
    return reduce(lambda x, y: x+y, input_list)
