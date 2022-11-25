N = int(input())
M = int(input())

set_a = set()
set_b = set()

for i in range(N):
    set_a.add(input())
for i in range(M):
    set_b.add(input())

if len(set_a & set_b) != 0:
    print(len(set_a & set_b))
else:
    print("Таких нет")