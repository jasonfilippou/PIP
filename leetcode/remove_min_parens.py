# Source: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
#
# The logic of this solution is to keep a counter of the difference of #scanned left parens - #scanned right parens.
# If the counter drops below 0, then we have an unmwatched right paren, and it definitely needs to be removed.
# At the end of our scan, if our counter is > 0, we need to remove the last counter-many left parentheses, so we
# scan the string once more from end to start to remove those.
#
#  "Removal" in our case consists of a boolean vector that tells us which characters we want to keep.
#
#   Time complexity: Linear in length of string.
#   Space complexity: Linear in length of string.

from typing import List


def minimally_balance_string(s: str) -> str:
    height = 0
    keep_char = [False for _ in range(len(s))]
    for i in range(len(s)):
        if s[i] == '(':
            height += 1
            keep_char[i] = True
        elif s[i] == ')':
            if height > 0:
                height -= 1
                keep_char[i] = True     # Otherwise keep it at False, we don't touch the array
        else:
            keep_char[i] = True         # Simply maintain other characters
    if height > 0:
        _erase_dangling_left_parens(s, height, keep_char)
    return _reduce_string(s, keep_char)


def _erase_dangling_left_parens(s: str, height: int, keep_char: List[bool]):
    i = len(s) - 1
    while i > -1 and height > 0:            # We erase the last height - many left parens!
        if s[i] == '(':
            keep_char[i] = False
            height -= 1
        i -= 1


def _reduce_string(s: str, keep_char: List[bool]) -> str:
    reduced_string = []
    for i in range(len(s)):
        if keep_char[i] is True:
            reduced_string.append(s[i])
    return ''.join(reduced_string)


if __name__ == '__main__':
    for s in ["()", "b(a)r)", ")(", "(((((", ")(())(", "(()()(", "(())())", "J(ason", "J(a(s)o)n", "J(a(s)on",
              "(((((((memes)))()", "(m o) (r e ) (m e ( m e ) ( ) ( )s", "))))))()((((((())("]:
        print(minimally_balance_string(s))
