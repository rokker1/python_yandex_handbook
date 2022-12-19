def to_string(*args, sep=" ", end="\n"):
    res = ""
    res = sep.join([str(arg) for arg in args])
    res += end
    return res

print(to_string(1, 2, 3))
data = [7, 3, 1, "hello", (1, 2, 3)]
print(to_string(*data, sep=", ", end="!"))