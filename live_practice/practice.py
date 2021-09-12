def bin_search(arr, x):
    return bin_search_rec(arr, x, 0, len(arr) - 1)


def bin_search_rec(arr, x, left, right):
    if left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return bin_search_rec(arr, x, left, mid - 1)
        else:
            return bin_search_rec(arr, x, mid + 1, right)
