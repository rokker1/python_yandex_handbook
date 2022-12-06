with open("/home/alexander/source/python_yandex_handbook/3.Collections/3.5.iostream/input_1.txt", encoding="UTF-8") as file_in:
    for line in file_in:
        print(line.rstrip("\n"))

with open("/home/alexander/source/python_yandex_handbook/3.Collections/3.5.iostream/input_1.txt", encoding="UTF-8") as file_in:
    lines = file_in.readlines()
print(lines)

with open("/home/alexander/source/python_yandex_handbook/3.Collections/3.5.iostream/input_1.txt", encoding="UTF-8") as file_in:
    symbols = file_in.read(10)
print(symbols)

with open("/home/alexander/source/python_yandex_handbook/3.Collections/3.5.iostream/output_1.txt", "w", encoding="UTF-8") as file_out:
    n = file_out.write("Это первая строка\nА вот и вторая\nИ третья — последняя\n")
print(n)

lines = ["Это первая строка\n", "А вот и вторая\n", "И третья — последняя\n"]
with open("/home/alexander/source/python_yandex_handbook/3.Collections/3.5.iostream/output_1.txt", "w", encoding="UTF-8") as file_out:
    file_out.writelines(lines)

with open("/home/alexander/source/python_yandex_handbook/3.Collections/3.5.iostream/output_1.txt", "w", encoding="UTF-8") as file_out:
    print("вывод в файл с помощью функции print():", file=file_out)

