import itertools

goods = [input().split(", ") for i in range(int(input()))]

for i in itertools.permutations(sorted(itertools.chain.from_iterable(goods)), r=3):
    print(", ".join(i))
