import itertools

a = int(input())
b = int(input())
for i in range (0, a):
    print(" ".join(str(b * j[0] + j[1]) for j in itertools.product([i], range(1, b + 1))))