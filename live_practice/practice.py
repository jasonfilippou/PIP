from typing import List

def skip_skip_action_template(arr:List[int]):
    l, r = 0, 0
    while l <= r:
        if mustSkip(l, arr):
            l += 1
        elif mustSkip(r, arr):
            r -= 1
        else:
            action()
            l += 1
            r -= 1

def compare_action_advance_template(arr1:List[int], arr2: List[int]):           # This one needs 2 iterables
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if behind(i, j):
            action1()
            i += 1
        elif behind(j, i)
            action2()
            j += 1
        else:
            action3()
            i += 1
            j += 1

def read_write_template(arr:List[int]):
    wp, rp = 0, 0
    while rp < len(arr):
        if must_write(rp, arr):
            arr[wp] = arr[rp]
            wp += 1
        rp += 1