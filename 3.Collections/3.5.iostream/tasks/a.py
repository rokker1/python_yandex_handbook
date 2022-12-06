from sys import stdin

lines = []
for line in stdin:
    lines.extend([int(x) for x in line.rstrip('\n').split()])
print(sum(lines))