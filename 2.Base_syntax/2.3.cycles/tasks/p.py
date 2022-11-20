n = input()
f = True
for i in range(len(n)):
    if n[i] != n[len(n) - 1 - i]:
        f = False
        break

if f:
    print("YES")
else:
    print("NO")