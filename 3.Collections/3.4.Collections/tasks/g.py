from itertools import combinations

kids = [input() for i in range(int(input()))]

for v in combinations(kids, r=2):
    print(f"{v[0]} - {v[1]}")
