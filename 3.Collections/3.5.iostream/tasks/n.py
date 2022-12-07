import json
from sys import stdin


in_file = stdin.readline().rstrip("\n")
updates_file = stdin.readline().rstrip("\n")

workdir = "/home/alexander/source/python_yandex_handbook/3.Collections/3.5.iostream/tasks/"
with open(workdir + in_file, "r", encoding="UTF-8") as in_f:
    data = json.load(in_f)

result_data = {}
with open(workdir + updates_file, "r", encoding="UTF-8") as upd_f:
    updates = json.load(upd_f)
    for user in updates:
        name = user.get("name")
        # print(name)
        existing_found = False
        for existing_user in data:
            # print(existing_user["name"])
            if existing_user["name"] == name:
                # print("good")
                existing_found = True
                result_data[name] = existing_user.copy()
                del result_data[name]["name"]

                for k, v in user.items():
                    if k != "name":
                        if k in result_data[name]:
                            result_data[name][k] = max(result_data[name][k], v)
                        else:
                            result_data[name][k] = v

with open(workdir + in_file, "w", encoding="UTF-8") as out_file:
    json.dump(result_data, out_file, ensure_ascii=False)

print(result_data)
            
