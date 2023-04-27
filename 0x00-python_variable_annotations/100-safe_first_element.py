#!/usr/bin/env python3
'''duck-typing a given function'''
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''the function to be duck-typed'''
    if lst:
        return lst[0]
    else:
        return None
