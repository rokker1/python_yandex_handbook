from itertools import product

kinds = ["треф", "пик", "бубен", "червей"]
nominals = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]

sub = input()



for value in product(nominals, [kind for kind in kinds if kind != sub]):
    print(f"{value[0]} {value[1]}")
    