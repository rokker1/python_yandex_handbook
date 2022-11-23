n = int(input())


def is_prime(a):
    flag = True
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            flag = False
            break
    if flag and a != 1:
        return True
    else:
        return False


def build_prime_numbers(n):
    prime_numbers = []
    # print(int(n ** 0.5))
    for i in range(2, int(n * 0.5) + 1):
        if is_prime(i):
            prime_numbers.append(i)
    return prime_numbers


prime_numbers = build_prime_numbers(n)
# print(prime_numbers)

m = []
while n != 1:
    for prime_number in prime_numbers:
        if n % prime_number == 0:
            m.append(prime_number)
            n = n / prime_number
            break

is_first = True
for p in m:
    if not is_first:
        print(" * ", end="")
    is_first = False
    
    print(p, end="")