def merge(lhs, rhs):
    merged = []
    lindex = 0
    rindex = 0
    while not (lindex == len(lhs) or rindex == len(rhs)):
        if lhs[lindex] > rhs[rindex] and rindex != len(rhs):
            merged.append(rhs[rindex])
            rindex += 1
        else:
            merged.append(lhs[lindex])
            lindex += 1
    if lindex != len(lhs):
        merged.extend(lhs[lindex:])
    elif rindex != len(rhs):
        merged.extend(rhs[rindex:])
    return tuple(merged)

print(merge((1, 2), (3, 4, 5)))