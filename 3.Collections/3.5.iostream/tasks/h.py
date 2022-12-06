from sys import stdin

args = stdin.readlines()
args = [arg.rstrip("\n") for arg in args]

set_a = set()
set_b = set()

directory = "f:/source/python_yandex_handbook/3.Collections/3.5.iostream/tasks/"


def read_file_to_set(filename, set_):
    with open(directory + filename, "r", encoding="UTF-8") as file_a:
        for line in file_a:
            for word in line.split():
                set_.add(word)

read_file_to_set(args[0], set_a)
read_file_to_set(args[1], set_b)

set_c = set_a ^ set_b
with open(directory + args[2], "w", encoding="UTF-8") as file_a:
    for word in sorted(set_c):
        print(word, file=file_a)

