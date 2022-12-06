import itertools

n = int(input())

for a, b in enumerate(sorted(itertools.chain.from_iterable([input().split(", ") for i in range(n)]))):
    print(f"{a + 1}. {b}")