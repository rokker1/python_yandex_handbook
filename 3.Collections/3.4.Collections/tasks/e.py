import itertools

line_a = input().split(", ")
line_b = input().split(", ")
line_c = input().split(", ")

for k, v in enumerate(sorted(itertools.chain(line_a, line_b, line_c)), start=1):
    print(f"{k}. {v}")