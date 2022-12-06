from itertools import islice
from itertools import cycle

foods = [input() for i in range(int(input()))]
for f in islice(cycle(foods), 0, int(input())):
    print(f)