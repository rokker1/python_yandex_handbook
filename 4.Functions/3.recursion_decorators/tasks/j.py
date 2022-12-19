def make_linear(l):
    res = []
    for element in l:
        if isinstance(element, list):
            res.extend(make_linear(element))
        else:
            res.append(element)
    return res


result = make_linear([1, [2, [3, 4]], 5, 6])
print(result)