line = input()
archive = []
while len(line) != 0:
    if len(line) > 1:
        repeated_char = line[0]
        repeated_char_count = 1
        line = line[1:]
        while (len(line) > 0 and line[0] == repeated_char):
            repeated_char_count += 1
            line = line[1:]
        archive.append((repeated_char, repeated_char_count))

    else:
        archive.append((line[0],1))
        line = line[1:]

for t in archive:
    print(f"{t[0]} {t[1]}")