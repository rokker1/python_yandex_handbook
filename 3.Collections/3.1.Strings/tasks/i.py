while line := input():
    pos = line.find("#")
    if pos == -1:
        print(line)
    elif pos > 0:
        print(line[:pos])