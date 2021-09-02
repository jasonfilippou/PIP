"""
We are given an array of integers that represent temperatures. For example:

A = [73, 74, 75, 71, 69, 72, 76, 73].

Create and return an array of the same length, where every element will contain the number of days until the next (strictly)
warmer day. For example, for the array above, the array we would want is:

res = [1, 1, 4, 2, 1, 1, 0, 0]
"""
from typing import List

'''
Will avoid naive quadratic algorithm with a stack-based approach that loops from end to finish.
'''

class Solution:
    def nextWarmerDay(self, temps: List[int]) -> List[int]:
        assert temps is not None
        ret_val = [0] * len(temps)
        stack = []
        for i in range(len(temps) - 1, -1, -1):
            while len(stack) > 0 and temps[stack[-1]] <= temps[i]:
                stack.pop()
            ret_val[i] = 0 if len(stack) == 0 else (stack[-1] - i)    # Guaranteed positive because we scan from right to left.
            stack.append(i)
        return ret_val


if __name__ == '__main__':
    soln = Solution()
    for arr in [[],
                [100],
                [70, 71],
                [71, 70],
                [70, 70],
                [51, 53, 54],
                [0, 0, -1],
                [49, 40, 90],
                [25, 100, 89, 38, 29, 90, 67, 30, 78, 32],
                [73, 74, 75, 71, 69, 72, 76, 73]
                ]:
        print(f"Temperatures {arr} map to array {soln.nextWarmerDay(arr)}.")
