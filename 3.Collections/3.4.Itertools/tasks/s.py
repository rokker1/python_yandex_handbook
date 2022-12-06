import itertools
program  = input()
variables_list = set([x for x in program.split() if len(x) == 1 and x.isupper()])
variables_list = sorted(list(variables_list))
print(" ".join(variables_list), "F", sep=" ")
for x in (itertools.product([False, True], repeat=len(variables_list))):
    print(" ".join([str(int(i)) for i in x]), str(int(eval(program, dict(zip(variables_list, x))))))