N = int(input())
numbers = []
for i in range(N):
    n = int(input())
    numbers.append(n)
P = int(input())
result = [i ** P for i in numbers]
for i in result:
    print(i)