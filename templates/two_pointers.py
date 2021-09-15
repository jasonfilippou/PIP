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
    return True if ptr % 2 == 0 else False


def action():
    print("Action!")
