from functools import lru_cache


def fibonacci(n):

    @lru_cache(maxsize=1000)
    def f(n):
        if n == 0:
            return 0
        
        if n == 1:
            return 1

        return f(n - 2) + f(n - 1)

    for i in range(0, n):
        yield f(i)


    
print(*fibonacci(10), sep=', ')