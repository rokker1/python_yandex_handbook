def make_equation(*args):
    if len(args) == 1:
        return str(args[0])
    result = f"({make_equation(*tuple(args[:-1]))}) * x + {args[-1]}"
    return result

print(make_equation(3, 2, 1))