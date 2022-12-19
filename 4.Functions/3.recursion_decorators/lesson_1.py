from timeit import timeit

def fact(n):
    if n == 0:
        return 1
    return fact(n - 1) * n

def fib(n):
    global count
    count += 1
    if n in (0, 1):
        return 1
    return fib(n - 1) + fib(n - 2)

count = 0
# print(fib(10))

print(f"Среднее время вычисления: "
      f"{round(timeit('fib(35)', number=10, globals=globals()) / 10, 3)} с.")
print(count)