n = input()
res = ""
for i in range(len(n)):
    if int(n[i]) % 2 != 0:
        res += n[i]
print(res)