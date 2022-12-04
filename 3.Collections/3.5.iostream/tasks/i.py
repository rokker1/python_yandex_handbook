from sys import stdin

args = stdin.readlines()
args = [string.rstrip("\n") for string in args]
directory = "f:/source/python_yandex_handbook/3.Collections/3.5.iostream/tasks/"
with open(directory + args[0], "r", encoding="UTF-8") as input_file,\
        open(directory + args[1], "w", encoding="UTF-8") as output_file:
    lines = [line for line in input_file.read().expandtabs(tabsize=1).splitlines() if line != '' and not line.isspace()]
    for line in lines:
        print(" ".join(line.split()), file=output_file)

print(0)