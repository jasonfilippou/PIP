"""
Bottom - up knapsack,
with solution reconstruction.
"""


def knapsack(values, weights, W):
    assert len(values) == len(weights), "Values and weights arrays should have the same length."
    n = len(values)
    opt_profit = [ [0 for _ in range(W + 1)] for _ in range(n+1)]    # (n+1) x (W+1) array of zeroes. First row and col stay zero.
    for i in range(1, n+1):
        item_weight = weights[i - 1]
        item_value = values[i - 1]
        for j in range(1, W+1):
            if j < item_weight:
                opt_profit[i][j] = opt_profit[i - 1][j]
            else:
                opt_profit[i][j] = max(opt_profit[i - 1][j], item_value + opt_profit[i - 1][j - item_weight])

    # We will also reconstruct the solution.
    items_included = []                          # preallocate for speed of subsequent insertions.
    i, j = n, W
    while i > 0:                                 # If we reach the first row, we are done; the first row corresponds to no item selection.
        if opt_profit[i][j] != opt_profit[i - 1][j]:
            items_included.append(i)             # 1-index the items for readability.
            j -= weights[i - 1]
        i -= 1                                   # row index gets incremented no matter what.
    items_included.reverse()                     # Not necessary, but improves readability.
    return opt_profit, items_included


if __name__ == '__main__':
    values = [10, 20, 15, 17]
    weights = [1, 3, 2, 2]
    W = 4
    profits, solution = knapsack(values, weights, W)

    print(f"Optimal profits:{profits}")
    print(f"Items included: {solution}")