line = input().split()
a = float(line[0])
b = float(line[1])
c = float(line[2])

from itertools import count

for value in count(a, c):
    if value <= b:
        print(round(value, 1))
    else:
        break
