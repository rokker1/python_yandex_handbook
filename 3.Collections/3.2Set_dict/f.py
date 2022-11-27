N = int(input())
M = int(input())

set_a = set()
set_b = set()

for i in range(N):
    set_a.add(input())
for i in range(M):
    set_b.add(input())

if len(set_a ^ set_b) != 0:
    sorted_surnames = sorted([x for x in set_a.symmetric_difference(set_b)])
    for surname in sorted_surnames:
        print(surname)
else:
    print("Таких нет")