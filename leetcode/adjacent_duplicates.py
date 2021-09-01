# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
from builtins import str
from typing import List


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if len(stack) > 0 and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)


if __name__ == '__main__':
    soln = Solution()
    strs = ["jason", "jaason", "jaajon", "poor", "teehee", "teeth", "teetheeh"]
    for s in strs:
        print(f"{s} --> {soln.removeDuplicates(s)}")
