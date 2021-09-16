# We will use a compare-action-advance template
from typing import List

def array_intersection(arr1: List[int], arr2: List[int]):
    arr1.sort()
    arr2.sort()
    res = []
    i1, i2 = 0, 0
    while i1 < len(arr1) and i2 < len(arr2):
        if arr1[i1] < arr2[i2]:
            i1 += 1
        elif arr1[i1] > arr2[i2]:
            i2 += 1
        else:
            res.append(arr1[i1])  # Or arr2[i2], they are the same value after all.and
            i1 += 1
            i2 += 1
    return res
        