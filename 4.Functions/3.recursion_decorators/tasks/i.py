def cycle(l):
    i = -1
    while(True):
        i += 1
        if i == len(l):
            i = 0        
        yield l[i]


print(*(x for _, x in zip(range(5), cycle([1, 2, 3]))))
