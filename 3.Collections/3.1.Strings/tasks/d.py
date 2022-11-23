while len(line := input()) != 0:
    if line.endswith("@@@"):
        continue
    elif line.startswith("##"):
        print(line[2:])
    else:
        print(line)