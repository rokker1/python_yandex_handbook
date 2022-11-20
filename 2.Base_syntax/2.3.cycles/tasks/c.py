a = int(input())
b = int(input())
ans = ""
s = 1

if a > b:
    s = -1
    b -= 1
elif a <= b:
    b += 1


for i in range(a, b, s):
    ans += (str(i) + " ")
print(ans)