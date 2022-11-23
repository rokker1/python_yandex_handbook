L = int(input())
N = int(input())
for line in range(N):
    line = input()
    if len(line) <= L:
        print(line)
    else:
        print(line[:L-3] + "...")