from typing import List


def binary_search_iter(arr: List[int], el: int) -> bool:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == el:
            return True
        elif arr[mid] > el:
            high = mid - 1
        else:
            low = mid + 1
    return False


def binary_search_rec(arr: List[int], el: int) -> bool:

    def helper(arr: List[int], el: int, start: int, end: int) -> bool:
        if start > end:
            return False
        mid = (start + end) // 2
        if arr[mid] == el:
            return True
        elif arr[mid] < el:
            return helper(arr, el, mid + 1, end)
        else:
            return helper(arr, el, start, mid - 1)

    return helper(arr, el, 0, len(arr) - 1)


if __name__ == '__main__':
    sorted_arrays = [
        [],
        [8],
        [9],
        [9, 9],
        [8, 9],
        [7, 8, 9],
        [9, 10, 11],
        [1, 9, 10],
        [8, 9, 20],
        [7, 8, 10, 11],
        [1, 3, 4, 9, 10, 13],
        [1, 2, 3, 4, 9, 10, 13],
        [0, 0, 1, 1, 1, 9, 10],
        [0, 0, 1, 1, 1, 10],
        [9, 9, 9, 9, 9, 9, 9, 10],
        [1]*1000 + [8]*1000 + [9] + [10]*1000000
    ]
    for (idx, arr) in enumerate(sorted_arrays):
        print(f"Searching array #{idx}: {binary_search_rec(arr, 9)}")
