# Note: all of my numbers are unsigned bytes.
from typing import List, Set, Tuple


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    accum = set()  # Make into tuple to allow it to be hashable.
    _backtrack(candidates, target, 0, tuple([]), accum)
    return list(accum)


def _backtrack(candidates: List[int], target: int, current_sum: int, current_candidates: Tuple[List[int]], accum: Set[Tuple[List[int]]]):
    if current_sum == target:
        accum.add(tuple(sorted(current_candidates)))  # sorting the candidate list allows us to find dups easy later.
    elif current_sum < target:
        for candidate in candidates:  # I am allowed to re-use candidates, so every stack frame examines all of them!
            _backtrack(candidates, target, current_sum + candidate, current_candidates + tuple([candidate]), accum)
    # We don't have a case for > since we don't want to further recurse in that case!


if __name__ == '__main__':
    print(combination_sum())