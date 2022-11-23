line = input()
numbers = [int(x) for x in line.split()]


def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


gcd = nod(numbers[0], numbers[1])

if len(numbers) > 2:
    for i in range(2, len(numbers) - 1):
        gcd = nod(gcd, numbers[i])

print(gcd)