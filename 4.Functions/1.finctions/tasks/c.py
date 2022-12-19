import math
def number_length(n):
    if n == 0:
        return 1
    n = abs(n)
    epsilon = 1e-15
    lenght = math.log(n, 10) + epsilon
    return math.floor(lenght) + 1



print(number_length(0))
print(number_length(1))
print(number_length(9))
print(number_length(1000))
print(number_length(9999))
print(number_length(10000))
print(number_length(99999))
print(number_length(100000))