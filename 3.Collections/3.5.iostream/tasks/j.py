from sys import stdin

args = stdin.readlines()
args = [string.rstrip("\n") for string in args]

directory = "f:/source/python_yandex_handbook/3.Collections/3.5.iostream/tasks/"
if int(args[1]) > 0:
    with open(directory + args[0], "r", encoding="UTF-8") as input_file:
        lines = input_file.readlines()
        first_line_index = len(lines) - int(args[1])
        for line in lines[max(0, first_line_index):]:
            print(line.rstrip("\n"))

