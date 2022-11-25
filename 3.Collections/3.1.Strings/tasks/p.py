L = int(input())
N = int(input())

headings = []
for i in range(N):
    line = input()
    headings.append(line)

result = []
for line in headings:
    if L > 0:
        if len(line) <= L - 3:
            result.append(line)
            L -= len(line)
        else:
            result.append(line[ : L - 3] + "...")
            L = 0

for line in result:
    print(line)