import itertools

print("А", "Б", "В")
n = int(input())
for i in range(1, n - 1):
    for j in range(1, n - i):
        print(i, j, n - i - j)