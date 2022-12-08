import itertools

N = int(input())

for i in range (1, N + 1):
    print(" ".join(str(i[0] * i[1]) for i in itertools.product([i], range(1, N + 1))))