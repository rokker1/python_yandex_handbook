def recursive_sum(*args):
    if len(args) == 0:
        return 0
    l = [x for x in args]
    return args[-1] + recursive_sum(*tuple(l[:-1]))



answer = recursive_sum(1,2,3)
print(answer)
 