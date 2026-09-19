"""
Sliding window is used to get contiguous subarray or substring that meets a certain condition.




"""

from typing import Any, List


def sliding_window(some_list: List[Any]):
    res = []
    l,r = 0,1
    some_condition = something = True
    while (r < len(some_list)):

        if (some_condition):
            l += 1
        else:
            r += 1
        if something:
            res = some_list[l:r]

    return res
        
