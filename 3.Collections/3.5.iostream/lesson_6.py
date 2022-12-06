import json

work_dir = "/home/alexander/source/python_yandex_handbook/3.Collections/3.5.iostream/"
filename = "data.json"

with open(work_dir + filename, encoding="UTF-8") as file_in:
    records = json.load(file_in)
records[1]["group_number"] = 121212121
with open(work_dir + filename, "w", encoding="UTF-8") as file_out:
    json.dump(records, file_out, ensure_ascii=False, indent=2)