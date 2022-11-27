N = int(input())
objects = set()
for i in range(N):
    line = input().split()
    for item in line:
        objects.add(item)
for item in objects:
    print(item)