count = 0
while (st := input()) != "Приехали!":
    if "зайка" in st:
        count += 1
print(count)