# https://leetcode.com/problems/valid-parentheses/
from builtins import str


class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        for c in s:
            if _isOpeningBracket(c):
                my_stack.append(c)  # An invariant of this algorithm is that closing brackets
            elif _isClosingBracket(c):  # are NEVER pushed on the stack; they only pop opening
                if len(my_stack) == 0 or not _matches(my_stack[-1], c):  # brackets.
                    return False
                elif _matches(my_stack[-1], c):
                    my_stack.pop()
            else:
                raise AssertionError(f"Input string contained invalid character {c}")
        return len(my_stack) == 0


def _isOpeningBracket(c):
    return c in "([{"


def _isClosingBracket(c):  # could also define as `not _isOpeningBracket`, but this is more robust towards
    return c in "}])"  # strings that contain other characters.


def _matches(opening_bracket, closing_bracket):
    return (opening_bracket == '{' and closing_bracket == '}') or \
           (opening_bracket == '(' and closing_bracket == ')') or \
           (opening_bracket == '[' and closing_bracket == ']')


if __name__ == '__main__':
    s = Solution()
    strs = ["()", "[]", "{}", "()()", "()(", "())", "([])", "([])()", "{[()]}", "([])({{}()}[[[]]])"]
    for str in strs:
        print(f"{str} is valid: {s.isValid(str)}")
