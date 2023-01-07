from math import log, pow, cos, sin, pi, e

x = float(input())
result = log((pow(x, 3 / 16)), 32) + pow(x, cos((pi - x) / (2 - e))) - pow(sin(x / pi), 2)
print(result)