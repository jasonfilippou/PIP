'''
https://leetcode.com/problems/house-robber

A classic, easy one-dimensional DP problem, solvable in linear time and space.
'''
from typing import List


def rob_tabulate(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    elif len(nums) < 3:     # 1 or 2
        return max(nums)    # With 1 house, just return its own money stashed. With 2 houses, can't rob both because police will be alerted. Pick one with most money.
    max_gains = [0 for _ in range(len(nums))]
    max_gains[0] = nums[0]
    max_gains[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        max_gains[i] = max(max_gains[i - 2] + nums[i], max_gains[i - 1])
    return max_gains[-1]

### The memoized implementation is prone to stack overflow errors during the first recursive call.
def rob_memoize(nums: List[int]) -> int:

    memo = [-1 for _ in range(len(nums))]
    memo[0], memo[1] = nums[0], max(nums[0], nums[1])

    def helper(nums: List[int], idx: int):
        if idx >= 2 and memo[idx] == -1:
            memo[idx] = max(helper(nums, idx - 1), helper(nums, idx - 2) + nums[idx])
        return memo[idx]

    return helper(nums, len(nums) - 1)

### The following is a demonstration of why rob() with DP is so efficient. If we don't store the maximum gains up to a point
### in the array, we have to re-calculate it every time, like in Fibonacci.
def rob_inefficient(nums: List[int]) -> int:

    def helper(nums: List[int], idx:int):
        if idx == 0:
            return nums[0]
        elif idx == 1:
            return max(nums[0], nums[1])
        else:
            return max(helper(nums, idx - 1), helper(nums, idx - 2) + nums[idx])  # Recursive calls. Good luck.

    return helper(nums, len(nums) - 1)


if __name__ == '__main__':
    for arr in [
                [1, 2, 3, 1],
                [2, 7, 9, 3, 1],
                [10, 5, 20, 25],
                [5, 10, 1, 24, 9, 7, 45, 10, 7, 10, 7, 7, 5, 10]
                ]:
        print(f"Tabulation: Maximum gains from robbing house lane {arr} are: {rob_tabulate(arr)}")
        print(f"Memoization: Maximum gains from robbing house lane {arr} are: {rob_memoize(arr)}")
        print(f"Inefficient: Maximum gains from robbing house lane {arr} are: {rob_inefficient(arr)}")

