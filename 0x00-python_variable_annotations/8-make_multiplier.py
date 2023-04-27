#!/usr/bin/env python3
'''Module contains annotated function that returns a callable type'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''function takes a float returns a callable'''
    def float_multiplier(mul: float) -> float:
        '''function takes a float and multiplier with a float'''
        return mul * multiplier
    return float_multiplier
