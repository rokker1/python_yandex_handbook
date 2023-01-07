from collections.abc import Iterable


def check_sort(arg):
    if isinstance(arg, str):
        if len(arg) > 1:
            for i in range(len(arg) - 1):
                if arg[i] > arg[i + 1]:
                    return False
        return True
    return sorted(arg) == arg


def merge(lhs, rhs):
    if not (isinstance(lhs, Iterable) and isinstance(rhs, Iterable)):
        raise StopIteration
    lhs = list(lhs)
    rhs = list(rhs)
    merged = []
    lindex = 0
    rindex = 0
    while not (lindex == len(lhs) or rindex == len(rhs)):
        if not isinstance(lhs[lindex], type(rhs[rindex])):
            raise TypeError
        if len(lhs) != 0:
            t = type(lhs[lindex])
        elif len(rhs) != 0:
            t = type(rhs[rindex])
        if lhs[lindex] > rhs[rindex] and rindex != len(rhs):
            merged.append(rhs[rindex])
            rindex += 1
        else:
            merged.append(lhs[lindex])
            lindex += 1
    if len(lhs) != 0 and len(rhs) != 0:
        for e in lhs[lindex:]:
            if not isinstance(e, t):
                raise TypeError
        for e in rhs[rindex:]:
            if not isinstance(e, t):
                raise TypeError
    if lindex != len(lhs):
        merged.extend(lhs[lindex:])
    elif rindex != len(rhs):
        merged.extend(rhs[rindex:])
    
    if not check_sort(lhs) or not check_sort(rhs):
        raise ValueError
    
    return tuple(merged)