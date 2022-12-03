import json

work_dir = "/home/alexander/source/python_yandex_handbook/3.Collections/3.5.iostream/"
filename = "data.json"

with open(work_dir + filename, encoding="UTF-8") as file_in:
    records = json.load(file_in)
print(records)