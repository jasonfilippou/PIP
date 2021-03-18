# We are given a positive integer n, which we want to reduce to 1. The rules are:
#   If the number is a multiple of 3, we *can* divide it by 3 (but we don't necessarily *have to*)
#   If the number is a multiple of 2, we *can* divide it by 2 (but we don't necessarily *have to*)
#   If the number is neither a multiple of 3 nor a multiple of 2, we can (and have to) subtract it by 1.
#
#  Find the *minimum* number of operations (divisions and subtractions) that are required to reduce a number to 1.
#
#   Examples:
#       (*) For n = 2, only 1 operation is needed, either divide by 2 or subtract by 1.
#
#       (*) For n = 7, we can subtract by 1 to reach 6. Now we can divide by either 2 or 3, and in both situations
#       we will reach a multiple of 2 or 3, so another division will do the trick for us. There is no shorter solution.
#
#       (*) For n = 15, we can divide by 3 to reach 5, subtract 1 to reach 4, then reach 1 with 2 divisions. 4 operations.
#       There is no shorter solution: subtracting 1 leads us to 14, which we can reduce to 7 with a division by 2,
#       and from the second example we know that now we will need 3 more operations, for a total of 5.
#       Or, we could avoid dividing by 2 when we reach 14 and instead subtract by 1 again. But now we are at 13, a prime.
#       So we have to subtract by 1 again. We are at 12 and already have counted 3 operations. Whether we reduce to 4 by
#       dividing by 3, 6 by dividing by 2 or we subtract by 1 again, we have 4 operations and not reached 1 yet. So
#       4 is minimal.


def min_steps(n):
    min_steps = [0 for _ in range(n + 1)]  # I don't want to use steps[0], and I *do* want to use steps[n]
    num_in_step = [0 for _ in range(len(min_steps))]    # num_in_step[i] = the integer that we will reach after we apply the operation selected
    min_steps[1] = 0  # Nothing to do
    min_steps[2] = 1  # Either subtracting 1 or div by 2
    min_steps[3] = 1  # By div by 3
    num_in_step[1] = 1
    num_in_step[2] = 1
    num_in_step[3] = 1
    if 0 < n < 4:
        return min_steps[n], num_in_step[n:0:-1]
    for i in range(4, n + 1):
        if i % 6 == 0:  # Div by 6? More than 2 options
            _update_min_cost(i, min_steps, num_in_step,  [i // 3, i // 2, i - 1])
        elif i % 3 == 0:  # By 3, but not by 2
            _update_min_cost(i, min_steps, num_in_step,  [i // 3, i - 1])
        elif i % 2 == 0:  # By 2, but not by 3
            _update_min_cost(i, min_steps, num_in_step,  [i // 2, i - 1])
        else:
            _update_min_cost(i, min_steps, num_in_step,  [i - 1])  # No other options
    return min_steps[n], _backtrace(num_in_step)


def _update_min_cost(num, min_steps_array, num_in_step_array, options):
    option_costs = [min_steps_array[option] for option in options]
    min_cost, idx = _min_and_argmin(option_costs)          # The minimum cost
    min_steps_array[num] = 1 + min_cost
    num_in_step_array[num] = options[idx]                  # Since the two arrays are in concordance by construction.


def _min_and_argmin(my_list):
    assert len(my_list) > 0, "Can't ask me for the argmin of an empty list"
    minimum_val = my_list[0]
    idx_of_minimum_val = 0
    for i in range(1, len(my_list)):
        if my_list[i] < minimum_val:
            minimum_val = my_list[i]
            idx_of_minimum_val = i
    return minimum_val, idx_of_minimum_val


def _backtrace(array):
    assert len(array) > 0, "Array should be non - empty."
    trace = []
    num = array[-1]
    while num > 1:
        trace.append(str(num))  # Stringifying so that I can print easily later
        num = array[num]
    trace.append('1')
    return ', '.join(trace)


if __name__ == '__main__':
    for num in [4, 10, 15, 22, 40]:
        num_min_steps, min_sol = min_steps(num)
        print(f"{num} can be reduced to 1 in {num_min_steps} steps: {min_sol}")