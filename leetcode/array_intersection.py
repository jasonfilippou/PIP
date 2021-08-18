# https://leetcode.com/problems/intersection-of-two-arrays-ii/

"""
JASON'S NOTES

- Naive solution consists of grabbing every integer from one array, and, if you find it in the other array, somehow mark the position where you found it as "used"
(for example, with another boolean array), so that it's not used as a match by possible duplicates of the integer.

Suppose n is the length of the larger array and m is the length of the smaller array. We start with the larger array. This has space complexity O(mtime complexity O(n * m), where n is the length of the array you choose to pick the integers from. Quadratic on `m`, linear on `n`. It would be better
if we started with the bigger array, so that n > m. But still, we should do better.

If I sort both arrays, in time O(nlog_2n + mlog_2m), I can spend linear time (O(m + n)) to compute the intersection, by using a two - pointer approach. The fact that we are
swapping the order of the elements in the arrays themselves does not matter at all, since these lists are literally being treated like sets, the order of the elements does not matter.

Examples from Leetcode after sorting the arrays:

nums1 = [1, 1, 2, 2]
nums2 = [2, 2]


nums1 = [4, 5, 9]
nums2 = [4, 4, 8, 9, 9]

So it seems as if we need two pointers that will advance from 0 to the end of their respective strings. Call them ptr1 and ptr2. We will run a loop that will stop when either one
of the pointers reaches the end of their respective string. Inside the loop, we will compare nums1[ptr1] and nums2[ptr2]. Three cases:

    - If they are equal, push the integer to the result list and advance both pointers.
    - Otherwise, if nums1[ptr1] is greater than nums2[ptr2], advance ptr2.
    - Otherwise, advance ptr1

Complexity: O(mlog_2m + nlog_2n + m + n) = O(nlog_2n). Whether the solution is better than O(n*m) depends on whether m is greater than log_2n or not :) The leetcode page
also has some interesting questions about what would happen if the m-sized array was stored in secondary storage.
"""
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1.sort()    # Might have linear space complexity depending on underlying sorting algorithm.
        nums2.sort()    # Same thing about space complexity.
        ptr1, ptr2 = 0, 0
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            # skip-skip-action
            if nums1[ptr1] > nums2[ptr2]:
                ptr2 += 1                       # Second array values have to catch up.
            elif nums1[ptr1] < nums2[ptr2]:
                ptr1 += 1                       # Now the first array's values have to catch up!
            else:
                result.append(nums1[ptr1])      # or nums2[ptr2], doesn't matter
                ptr1 += 1
                ptr2 += 1
        return result


if __name__ == '__main__':
    s = Solution()
    for array_pair in [   # I'm only going to put ints between 0 and 1000 inclusive to respect the question's guidelines
                        ([1, 2, 2, 1], [2, 2]),        # Leetcode's first
                        ([4, 9, 5], [9, 4, 9, 8, 4]),  # Leetcode's second
                        ([0, 0, 0], [0, 0, 0]),        # Custom
                        ([1, 0, 5, 1, 1, 5, 0], [1, 1, 1, 1, 0, 0, 0, 5]),    # Custom
                        ([2, 3, 4], []),  # Custom
                       ]:
        print(s.intersect(array_pair[0], array_pair[1]))
