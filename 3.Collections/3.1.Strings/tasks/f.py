N = int(input())
sum = 0
for i in range(N):
    line = input()
    words = line.split()
    sum += words.count('зайка')

print(sum)