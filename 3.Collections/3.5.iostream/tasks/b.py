from sys import stdin
from statistics import mean

lines = [l.rstrip('\n').split() for l in stdin.readlines()]
growth = [int(el[2]) - int(el[1]) for el in lines]
print(round(mean(growth)))