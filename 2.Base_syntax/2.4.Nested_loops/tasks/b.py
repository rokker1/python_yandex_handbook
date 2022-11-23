n = int(input())
for i in range(1, n + 1):
    first = True
    line = ""
    for j in range(1, n + 1):
        print(f"{j} * {i} = {j * i}")