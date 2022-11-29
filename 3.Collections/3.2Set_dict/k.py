N = int(input())

people = {}
for i in range(N):
    surame = input()
    people[surame] = people.get(surame, 0) + 1

count = 0
for k, v in people.items():
    if v > 1:
        count += v
if count:
    for surname in [n for n in sorted(people) if people[n] > 1]:
        print(f"{surname} - {people[surname]}")
else:
    print("Однофамильцев нет")