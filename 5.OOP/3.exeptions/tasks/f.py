class NoSolutionsError(Exception):
    pass


class InfiniteSolutionsError(Exception):
    pass


def find_roots(a, b, c):
    if not all(isinstance(arg, (int, float)) for arg in (a, b, c)):
        raise TypeError
    discriminant = float(b**2 - 4 * a * c)
    if discriminant < 0:
        raise NoSolutionsError
    if a == 0 and b == 0:
        if c == 0:
            raise InfiniteSolutionsError
        else:
            raise NoSolutionsError

    if a == 0 and b != 0:
        x = (-c) / (b)
        return (x, x)

    x1 = (-b - discriminant**0.5) / (2 * a)
    x2 = (-b + discriminant**0.5) / (2 * a)
    return (x1, x2)


print(find_roots(45,6,0))



