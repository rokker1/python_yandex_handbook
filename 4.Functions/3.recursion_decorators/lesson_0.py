from timeit import timeit

def fact(n):
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial

print(fact(0))
print(fact(1))
print(fact(5))


def fib(n):
    f_1, f = 1, 1
    for i in range(n - 1):
        f_1, f = f, f_1 + f
    return f


print(f"Среднее время вычисления: "
        f"{round(timeit('fib(35)', globals=globals()) / 10, 3)} c." )

