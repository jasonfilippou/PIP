from random import randint
from time import time

'''
Rod cutting 

(1) Recursively 

(2) Top-down memoized
 
(3) Bottom - up tabulated
'''


def recursive_rod_cutting(prices, n):
    if n == 0:
        return 0
    max_profit = float("-inf")
    for i in range(1, n+1):
        max_profit = max(max_profit, prices[i - 1] + recursive_rod_cutting(prices, n - i))
    return max_profit


def memoized_rod_cutting(prices, n):

    # Compare and contrast the following implementation to the pure recursive one!
    def memoized_rod_cutting_aux(prices, n, optimal_profits):
        if optimal_profits[n] >= 0:                     # avoid costly recalculation
            return optimal_profits[n]

        if n == 0:
            return 0
        max_profit = float("-inf")
        for i in range(1, n + 1):
            max_profit = max(max_profit, prices[i - 1] + memoized_rod_cutting_aux(prices, n - i, optimal_profits))
        optimal_profits[n] = max_profit                 # cache for future calls
        return max_profit

    optimal_profits = [float("-inf")] * (n + 1)
    return memoized_rod_cutting_aux(prices, n, optimal_profits)


def tabulated_rod_cutting(prices, n):
    solution = [-1] * n
    opt_profit = [0] * (n+1)        # Also storing optimal profit for rod of length 0, which is 0.
    for j in range(1, n+1):         # For all possible rod split points
        current_best_profit = float("-inf")
        for i in range(0, j):       # To find the opt. profit at position j, we have to consider opt. profits for all i = 0, 1, ..., j - 1.
            if current_best_profit < prices[i] + opt_profit[j - i - 1]:
                current_best_profit = prices[i] + opt_profit[j - i - 1]
                solution[j - 1] = i + 1
        opt_profit[j] = current_best_profit
    return opt_profit, solution


def get_solution(solution):
    ret_val = []
    n = len(solution) - 1
    while n > 0:
        ret_val.append(solution[n])
        n = n - solution[n]
    ret_val.reverse()
    return ret_val


def fetch_random_prices(min_price, max_price, n):
    return sorted([randint(min_price, max_price) for _ in range(n)])

def curr_time_millis():
    return round(time() * 1000)  # In millis

if __name__ == '__main__':
    # prices = [1, 5, 8, 9]                     # Example from our slides
    # prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 34, 35, 40, 40, 42, 45, 49, 50, 52, 55, 60, 66, 66, 68, 68]   # An expanded example
    prices = list(set(fetch_random_prices(1, 2300, 10000)))      # For stress testing
    # print(f"There are {len(prices)} objects in our list.")
    # start = curr_time_millis()
    # opt_profit = recursive_rod_cutting(prices, len(prices))
    # print(f"recursive rod cutting: Optimal profit given provided price points was {opt_profit}, calculated in {curr_time_millis() - start} ms.")
    # start = curr_time_millis()
    # opt_profit = memoized_rod_cutting(prices, len(prices))
    # print(f"memoized rod cutting: Optimal profit given provided price points was {opt_profit}, calculated in {curr_time_millis() - start} ms.")
    start = curr_time_millis()
    opt_profit, solution = tabulated_rod_cutting(prices, len(prices))
    print(f"tabulated rod cutting: Optimal profit given provided price points was {opt_profit[-1]}, calculated via cut(s) of lengths: {get_solution(solution)}, in {curr_time_millis() - start} ms.")


