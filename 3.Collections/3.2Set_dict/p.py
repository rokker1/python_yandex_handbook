answer = set()
while (line := input()) != "":
    items = line.split()
    while "зайка" in items:
        i = items.index("зайка")
        if i == 0:
            answer.add(items[1])
            items.remove("зайка")
        elif i == (len(items) - 1):
            answer.add(items[-2])
            items.remove("зайка")
        else:
            answer.add(items[i - 1])
            answer.add(items[i + 1])
            items.remove("зайка")

for item in sorted(answer):
    print(item)