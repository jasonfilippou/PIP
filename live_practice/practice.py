from typing import List, Set, Tuple


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    results = []

    def _backtrack(remain, comb, start):
        if remain == 0:
            results.append(comb)
            return
        elif remain < 0:
            # exceed the scope, stop exploration.
            return

        # The presence of the parameter "start" instead of the constant '0' is what makes this avoid duplicates.
        for i in range(start, len(candidates)):
            # give the current number another chance, rather than moving on
            _backtrack(remain - candidates[i], comb + [candidates[i]], i)

    _backtrack(target, [], 0)

    return results


if __name__ == '__main__':
    print(combinationSum([2, 3, 6, 7], 7))
    print(combinationSum([2, 3, 5], 8))
    print(combinationSum([2], 1))
