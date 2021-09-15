from typing import List

def binary_search_template_one(array:List[int], element:int):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] > element:
            right = mid - 1
        elif array[mid] < element:
            left = mid + 1
        else:
            return mid
    return -1

def binary_search_template_two(array:List[int], element:int):
    left, right = 0, len(array) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if array[mid] > element:
            right = mid
        elif array[mid] < element:
            left = mid
        else:
            return mid
    if array[left] == element:
        return left
    elif array[right] == element:   # So, if there are duplicates, we return the one at the leftmost index.
        return right
    else:
        return -1


