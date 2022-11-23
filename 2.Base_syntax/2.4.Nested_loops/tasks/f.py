N = int(input())


def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


result = 0
result = int(input())


for i in range(1, N):
    b = int(input())
    gcd = nod(result, b)
    result = gcd


print(result)