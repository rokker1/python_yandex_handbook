from timeit import timeit
from functools import lru_cache


@lru_cache(maxsize=1000)
def fib(n):
    if n in (0, 1):
        return 1
    return fib(n - 1) + fib (n - 2)


print(f"Среднее время вычисления: "
      f"{round(timeit('fib(35)', number=10, globals=globals()) / 10, 6)} с.")