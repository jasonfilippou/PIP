# https://leetcode.com/problems/evaluate-reverse-polish-notation/
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        assert tokens is not None and len(tokens) != 2, "With binary ops, we need 1 , 3 or more arguments."
        my_stack = []
        for i in range(len(tokens)):
            if _isOperator(tokens[i]):
                result = _evaluate(my_stack, tokens[i])
                my_stack.append(result)
            else:
                my_stack.append(int(tokens[i]))
        assert len(my_stack) == 1, "Stack should have a size of 1 at the end."
        return my_stack.pop()


def _isOperator(c):
    return c in "+-/*"


def _evaluate(my_stack, operator):
    assert len(my_stack) >= 2, "Stack should have at least size 2 when _evaluate() is called."
    rhs = int(my_stack.pop())  # Careful about which the RHS and LHS are!
    lhs = int(my_stack.pop())
    switcher = {
        '+': lhs + rhs,
        '-': lhs - rhs,
        '*': lhs * rhs,
        '/': int(lhs / rhs) if rhs != 0 else None
    }
    return switcher.get(operator, f"Invalid operator {operator}")


if __name__ == '__main__':
    solution = Solution()

    print(solution.evalRPN(['18']))
    print(solution.evalRPN(['1', '2', '+']))
    print(solution.evalRPN(['1', '2', '3', '+', '/']))
    print(solution.evalRPN(['-11', '-12', '/', '0', '*', '-1', '+', '1', '-', '1', '-15', '/', '-']))
