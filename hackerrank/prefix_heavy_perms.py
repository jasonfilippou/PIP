"""
Given two numbers n and k, with k < n, return the number of permutations of the numbers 1, 2, ...., n where the sum
of the first k numbers is strictly larger than the sum of the remaining numbers.

Constraints:
    (*) - 1 <= k < n < 10
"""


def prefix_heavy_permutations(n, k) -> int:
    ################################################################################################
    # Jason's notes:
    #
    # - In addition to the title of the problem section, two more things point to backtracking here:
    #
    #   * Small problem size. In fact, even a hyper-exponential solution will do here.
    #   * The fact that we are dealing with permutations. There are n! of those for a string of size n.
    #
    # - I will attempt this in Python for practice.
    #
    # - Logic: Generate all permutations. For every permutation, take the two slices, sum them, admit only the
    # prefix-heavy ones.
    #
    # - I did very badly on this. By 45 minutes I had only written a base case, and it wasn't working well. I had to
    # eventually Google how to find permutations recursively. I did it years ago in Prolog and don't remember much.
    # Haven't gone through the backtracking workshop either.

    # ###############################################################################################

    assert 0 < k < n, f"k={k}, n={n} are not appropriate values; we want k < n."
    return_list = list()
    find_admissible_permutations(n, k, 0, list(range(n)), return_list)  # range() is not inclusive of upper end,
    return len(return_list)                         # but subtracting every number by 1 does *not* # alter the solution.


def find_admissible_permutations(n, k, currDigitIdx, currentPermutation, validPermutations):
    if currDigitIdx == n:  # Exhausted permutation options. Check sums and admit accordingly.
        if sum(currentPermutation[0:k]) > sum(currentPermutation[k:]):  # Implicit linear space per stack frame
            validPermutations.append(currentPermutation)
    else:
        for i in range(currDigitIdx, n):  # From the current digit onward...

            # Notice that the first time this loop is entered, the below swapping does nothing.
            # This bodes well for the solution set, since the original string is also a valid permutation.
            currentPermutation[currDigitIdx], currentPermutation[i] = currentPermutation[i], currentPermutation[
                currDigitIdx]

            # Recursive call. Notice third argument: we have already "set" the i-th element; we want the other ones.
            find_admissible_permutations(n, k, i + 1, currentPermutation, validPermutations)

            # Swap again, since we counted all permutations for the previous swapped state. Time to swap the element
            # pointed to by "currDigitIdx" with something else, so that we cover all permutations.
            currentPermutation[currDigitIdx], currentPermutation[i] = currentPermutation[i], currentPermutation[
                                                                                                    currDigitIdx]
