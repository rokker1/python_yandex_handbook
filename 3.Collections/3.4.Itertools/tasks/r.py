import itertools

program = input()
print("a", "b", "c", "f", sep=" ")
for (a, b, c) in (itertools.product([False, True], repeat=3)):
    print(int(a), int(b), int(c), int(eval(program)))