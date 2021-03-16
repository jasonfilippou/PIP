from time import time


def fib_rec(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


# Memoized Fibonacci
def fib_mem(n: int) -> int:

    def algo_core(x, memo):
        if x in memo:
            return memo.get(x)
        else:
            memo[x] = algo_core(x - 1, memo) + algo_core(x - 2, memo)     # store once encountered
            return memo.get(x)

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo = {0: 0, 1: 1}             # map indices to values.
        return algo_core(n, memo)


# Tabulated Fibonacci
def fib_tab(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        array = [0, 1] + [0] * (n-1)
        for i in range(2, n+1):
            array[i] = array[i - 1] + array[i - 2]
        return array[-1]


# Helper for all experiments
def fibonacci_experiment(last_num, func):
    for i in range(0, last_num):
        fib_rec_start = round(time() * 1000)           # In millis
        val = func(i)
        print(f"Calculated fib({i}) = {val} using {func.__name__} in {round(time() * 1000) - fib_rec_start} milliseconds")


if __name__ == '__main__':
    # fibonacci_experiment(50, fib_rec)   # fib(0), fib(1), fib(30)
    # fibonacci_experiment(998, fib_mem)
    fibonacci_experiment(10000, fib_tab)
