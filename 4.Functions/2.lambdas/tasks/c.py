def gcd(*args):
    if len(args) == 1:
        return args[0]

    result = args[0]
    for i in range(1, len(args)):
        a = result
        b = args[i]
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        result = a + b

    return result


print(gcd(36))
print(gcd(36, 48))
print(gcd(36, 48, 156, 100500))
print(gcd(36, 48, 156, 100500, 15, 17, 26))