a = int(input())
s = 0
while (a != 0):
    s = max(s, a % 10)
    a = a // 10
print(s)