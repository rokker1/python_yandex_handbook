def is_prime(n):
    flag = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            flag = False
            break
    if flag and n != 1:
        return True
    else:
        return False