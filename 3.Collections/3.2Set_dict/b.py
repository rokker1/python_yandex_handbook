line_a = set(input())
line_b = set(input())
intersect = line_a & line_b
result = ""
for c in intersect:
    result += c
print(result)