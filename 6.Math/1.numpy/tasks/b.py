from sys import stdin
from math import gcd

lines = []
for line in stdin:
    print(gcd(*(int(x) for x in line.rstrip('\n').split())))
