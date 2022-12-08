from sys import stdin

args = stdin.readlines()
args = [s.rstrip("\n") for s in args]


def check_dacimal(decimal):
    even = 0
    odd = 0
    d = int(decimal)
    while d > 0:
        if (d % 10) % 2 == 1:
            odd += 1
        else:
            even += 1
        d //= 10
    
    if even > odd:
        return "even"
    elif even < odd:
        return "odd"
    else:
        return "eq"


work_dir = "f:/source/python_yandex_handbook/3.Collections/3.5.iostream/tasks/"
with open(work_dir + args[0], "r", encoding="UTF-8") as input_file,\
        open(work_dir + args[1], "w", encoding="UTF-8") as out_1,\
        open(work_dir + args[2], "w", encoding="UTF-8") as out_2,\
        open(work_dir + args[3], "w", encoding="UTF-8") as out_3:
    for line in input_file:
        evens = []
        odds = []
        eqs = []
        for decimal in line.rstrip("\n").split():
            check = check_dacimal(decimal)
            if check == "even":
                evens.append(decimal)
            elif check == "odd":
                odds.append(decimal)
            else:
                eqs.append(decimal)
        print(" ".join(evens), file=out_1)
        print(" ".join(odds), file=out_2)
        print(" ".join(eqs), file=out_3)
