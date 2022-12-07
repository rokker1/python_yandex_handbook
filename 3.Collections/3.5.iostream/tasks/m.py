from sys import stdin
import json

work_dir = "f:/source/python_yandex_handbook/3.Collections/3.5.iostream/tasks/"
filename = stdin.readline().rstrip("\n")
with open(work_dir + filename, "r", encoding="UTF-8") as out_file:
    data = json.load(out_file)
    
for line in stdin:
    items = line.rstrip("\n").split(" == ")
    data[items[0]] = items[1]

with open(work_dir + filename, "w", encoding="UTF-8") as out_file:
    json.dump(data, out_file, ensure_ascii=False)