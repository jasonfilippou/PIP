from numpy import argmin, argmax
from copy import deepcopy
MAX_HEAP = "maxheap"
MIN_HEAP = "minheap"


def heapify(arr, heap_type):

    def percolate_down(arr, i, heap_type):
        j = swap_and_return(arr, i, heap_type)
        while i != j:
            i = j
            j = swap_and_return(arr, i, heap_type)

    def swap_and_return(arr, i, heap_type):
        n = len(arr)
        indices_of_interest = [i, 2 * i + 1, 2 * i + 2]
        nodes_of_interest = [arr[x] for x in indices_of_interest if 0 <= x <= n-1]
        idx_to_swap = argmax(nodes_of_interest) if heap_type == MAX_HEAP else argmin(nodes_of_interest)
        arr[i], arr[indices_of_interest[idx_to_swap]] = arr[indices_of_interest[idx_to_swap]], arr[i]
        return indices_of_interest[idx_to_swap]

    try:
        if arr is None or len(arr) == 0:
            return []
    except ValueError:
        raise RuntimeError(f"Bad argument:{arr}")
    if heap_type is None or (heap_type != MAX_HEAP and heap_type != MIN_HEAP):
        raise RuntimeError(f"Arguments provided:arr={arr}, mode={heap_type}")
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):  # Linear time with good constant
        percolate_down(arr, i, heap_type)
    return arr


if __name__ == '__main__':
    for arr in [[],
                [10],
                [0],
                [-1],
                [1, 10],
                [10, 1],
                [10, -10],
                [10, -10, 0],
                [1, 1],
                [-1, -1],
                [10, 2, 3, 9, 2, 0, -2],
                [10, 5, 8, -1, 8, 10, 5, 9, 0, 10]]:
        print(f"Heapifying {arr} as maxheap: {heapify(deepcopy(arr), MAX_HEAP)}")
        print(f"Heapifying {arr} as minheap: {heapify(deepcopy(arr), MIN_HEAP)}")
