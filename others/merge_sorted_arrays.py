# Basically the merge() subroutine of mergesort.
from typing import  List


def merge(arr1: List[int], arr2: List[int]):
    ptr1, ptr2 = 0, 0
    i = 0
    res = [0 for _ in range(len(arr1) + len(arr2))]
    while ptr1 < len(arr1) and ptr2 < len(arr2):
        if arr1[ptr1] < arr2[ptr2]:
            res[i] = arr1[ptr1]
            ptr1 += 1
        else:
            res[i] = arr2[ptr2]
            ptr2 += 1
        i += 1
    while ptr1 < len(arr1):
        res[i] = arr1[ptr1]
        ptr1 += 1
        i += 1
    while ptr2 < len(arr2):
        res[i] = arr2[ptr2]
        ptr2 += 1
        i += 1
    return res


if __name__ == '__main__':
    arrays = [
                [[1, 2], [0, 3]],
                [[4, 6, 10], [10, 30, 35, 40]],
                [[11, 19, 20, 20, 20], [5, 13]],
                [[11, 20], [10, 13]],
                [[1, 2, 3, 5, 7, 8], [10, 13, 20, 50, 67, 80, 110]],
                [[], []],
                [[0], [0]],
                [[0], [1]]
            ]
    for array_pair in arrays:
        print(merge(array_pair[0], array_pair[1]))