from typing import List


def three_sum_closest(nums: List[int], target: int) -> int:
    nums.sort()
    closest_sum = float("inf")
    for idx in range(len(nums) - 2):
        num = nums[idx]
        left = idx + 1
        right = len(nums) - 1
        while left < right:
            s = num + nums[left] + nums[right]
            if abs(target - s) < abs(target - closest_sum):
                closest_sum = s
            # skip - skip - action
            if s > target:
                right -= 1
            elif s < target:
                left += 1
            else:
                return target
    return closest_sum


if __name__ == '__main__':
    # Leetcode example
    print(three_sum_closest([-1, 2, 1, -4], 1))         # Expecting 2

    # Our own example
    print(three_sum_closest([-1, 2, 1, -4], -5))        # Expecting -4

    # And another. Note that from the question constraints, there cannot be duplicate values in the array.
    # If there were a pair of duplicate values, there would be 2 solutions, and we are told there is 1.
    print(three_sum_closest([2, -4, 0, 10, 3], 8))      # Expecting 8