numbers = [number for number in range(16, 100, 4)]
print(set([x for x in numbers if (x == round((x ** 0.5)) ** 2)]))