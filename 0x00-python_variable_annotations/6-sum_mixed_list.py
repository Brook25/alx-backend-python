#!/usr/bin/env python3
'''annotatted funciton takes in a list of floats
and integers and returns a float
'''
from typing import List, Union
from functools import reduce


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''annotated function that takes a list of
    union of ints and floats
    '''
    return reduce(lambda x, y: x+y, mxd_lst)
