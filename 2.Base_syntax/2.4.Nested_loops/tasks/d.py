N = int(input())
sum = 0
for i in range(0, N):
    n = input()

    for i in range(0, len(n)):
        sum += int(n[i])

print(sum)