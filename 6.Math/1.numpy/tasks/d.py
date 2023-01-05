import math

numbers = [float(x) for x in input().split()]
avg_geom = math.pow(math.prod(numbers), 1 / len(numbers))
print(avg_geom)
