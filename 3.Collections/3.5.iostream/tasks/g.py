from statistics import mean

numbers = []
filename = input()
with open("f:/source/python_yandex_handbook/3.Collections/3.5.iostream/tasks/" + filename, "r", encoding="UTF-8") as input_file:
    for line in input_file:
        numbers.extend([int(x) for x in line.rstrip('\n').split()])
print(len(numbers))
print(len([number for number in numbers if number > 0]))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(round(mean(numbers), 2))
