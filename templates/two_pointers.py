# skip-skip-action template:
from typing import List

def skip_skip_action_template(arr: List[int]):
    left, right = 0, len(arr) - 1
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

def compare_action_advance_template(arr1: List[int], arr2: List[int]):
    ptr1, ptr2 = 0, 0
    while ptr1 < len(arr1) and ptr2 < len(arr2):
        if is_behind(ptr1):
            action1()
            ptr1 += 1
        elif is_behind(ptr2):
            action2()
            ptr2 += 1
        else:
            action3()
            advance(ptr1, ptr2)

def is_behind(ptr: int) -> bool
    return True if ptr % 2 == 0 else False  # Example

def action1():
    print("action1!")

def action2():
    print("action2!")

def action3():
    print("action3!")

def advance(ptr1: int, ptr2: int):
    print(f"{ptr1} and {ptr2} advance!")