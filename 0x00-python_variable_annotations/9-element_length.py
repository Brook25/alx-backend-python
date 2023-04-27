#!/usr/bin/env python3
'''Module contains functions for duck-typing'''
from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''funciton to be duck typed'''
    return [(i, len(i)) for i in lst]
