from sys import stdin
from statistics import mean

lines = []
for line in stdin:
    if line.strip(" ").startswith("#"):
        continue
    comment_pos = line.find("#")
    if comment_pos != -1:
        lines.append(line[:comment_pos].rstrip("\n"))
    else:
        lines.append(line.rstrip("\n"))

for line in lines:
    print(line)