from typing import List
'''
 The skip-skip action is useful in problems such as: "find if a String is palindromic".
'''
def skip_skip_action_template(arr: List[int]):
    left, right = 0, len(arr) - 1   # Opposite ends
    while left < right:
        if need_to_skip(left):
            left += 1
        elif need_to_skip(right):
            right -= 1
        else:
            action()
            left += 1
            right -= 1

def need_to_skip(ptr: int) -> bool:
    return True if ptr % 2 == 0 else False  # Example

def action():
    print("Action!")


'''
The Compare-Action-Advance template is useful for problems that involve two arrays with two different pointers.
A representative problem is "merge two sorted arrays", the merge() subroutine in mergesort.
'''

def compare_action_advance_template(arr1: List[int], arr2: List[int]):
    ptr1, ptr2 = 0, 0   # They both start from 0
    while ptr1 < len(arr1) and ptr2 < len(arr2):
        if is_behind(ptr1):
            action1()
            advance(ptr1)
        elif is_behind(ptr2):
            action2()
            advance(ptr2)
        else:
            action3()
            advance(ptr1, ptr2)

def is_behind(ptr: int) -> bool:
    return True if ptr % 2 == 0 else False  # Example

def action1():
    print("action1!")

def action2():
    print("action2!")

def action3():
    print("action3!")

def advance(ptr:int):
    print(f"{ptr} advances!")

def advance(ptr1: int, ptr2: int):
    print(f"{ptr1} and {ptr2} advance!")

'''
The Read-Write Pointer template is useful in problems of in-place modification.
'''

def read_write_template(arr:List[int]):
    wp, rp = 0, 0
    while rp < len(arr):
        if have_to_write(arr, rp):
            arr[wp] = arr[rp]
            wp += 1
        rp += 1
    return wp


def have_to_write(arr: List[int], rp: int):
    return True if rp % 2 == 0 else False # Example