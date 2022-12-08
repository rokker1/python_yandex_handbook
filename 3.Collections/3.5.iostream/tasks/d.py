from sys import stdin

input_lines = []
for line in stdin:
    input_lines.append(line.rstrip("\n"))
query = input_lines.pop(-1)
for line in input_lines:
    if query.lower() in line.lower():
        print(line)

    