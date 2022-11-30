import itertools

n = int(input())
for t in itertools.permutations(sorted([input() for i in range(n)])):
    print(", ".join(t))