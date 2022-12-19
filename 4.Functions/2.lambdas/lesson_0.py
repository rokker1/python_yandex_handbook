def add_value(x, list_arg=[]):
    list_arg += [x]
    return list_arg


print(add_value(0))
print(add_value(0, [1, 2, 3]))
print(add_value(1))
print(add_value(2))