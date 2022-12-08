from sys import stdin
import json

work_dir = "/home/alexander/source/python_yandex_handbook/3.Collections/3.5.iostream/tasks/"
filename = "f:/source/python_yandex_handbook/3.Collections/3.5.iostream/tasks/transliteration.txt"
with open(filename, "r", encoding="UTF-8") as in_file:
    trans_dict = dict()
    for line in in_file:
        letters = line.rstrip("\n").split(" — ")
        trans_dict[letters[0]] = letters[1]

with open("f:/source/python_yandex_handbook/3.Collections/3.5.iostream/tasks/transliteration.json", "w", encoding="UTF-8") as file_out:
    json.dump(trans_dict, file_out, ensure_ascii=False, indent=2)
print(trans_dict)