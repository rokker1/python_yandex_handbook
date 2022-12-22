print(";".join(str(1 / x) for x in range(int(input()), int(input()) + 1)))

start = input()
end = input()
if not (start.lstrip("-").isdigit() and end.lstrip("-").isdigit()):
    print("Необходимо ввести два числа.")
else:
    interval = range(int(start), int(end) + 1)
    if 0 in interval:
        print("Диапазон чисел содержит 0.")
    else:
        print(";".join(str(1 / x) for x in interval))

