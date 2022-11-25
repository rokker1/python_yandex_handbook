N = int(input())

kids = {}
for i in range(N):
    kid_info = input().split()
    name = kid_info[0]
    meals = kid_info[1:]
    kids[name] = meals
# print(kids)

query = input()

found = False
answer = []
for kid_info in kids.items():
    if query in kid_info[1]:
        answer.append(kid_info[0])
        found = True
if not found:
    print("Таких нет")
else:
    answer.sort()
    for name in answer:
        print(name)