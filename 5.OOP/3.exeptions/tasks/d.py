def only_positive_even_sum(a, b):
    
    try:
        if not (int(a) == a and int(b) == b and isinstance(a, int) and isinstance(b, int)):
            raise TypeError
    except Exception:
        raise TypeError
    if not (a >= 0 and a % 2 == 0 and b >= 0 and b % 2 == 0):
        raise ValueError
    return a + b