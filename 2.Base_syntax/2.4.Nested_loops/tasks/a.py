n = int(input())
for i in range(1, n + 1):
    first = True
    line = ""
    for j in range(1, n + 1):
        if not first:
            line += " "
        first = False
        line += str(i * j)
    print(line)