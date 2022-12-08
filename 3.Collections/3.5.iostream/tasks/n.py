import json
from sys import stdin

# in_file = stdin.readline().rstrip("\n")
# updates_file = stdin.readline().rstrip("\n")
in_file = "users.json"
updates_file = "updates.json"

# workdir = "/home/alexander/source/python_yandex_handbook/3.Collections/3.5.iostream/tasks/"
workdir = "/source/python_yandex_handbook/3.Collections/3.5.iostream/tasks/"
with open(workdir + in_file, "r", encoding="UTF-8") as in_f, open(workdir + updates_file, "r", encoding="UTF-8") as upd_f:
    data = json.load(in_f)
    updates = json.load(upd_f)
    result_data = {}
    for existing_user in data:
        existing_user_data = existing_user
        existing_user_name = existing_user["name"]
        del existing_user["name"]
        result_data[existing_user_name] = existing_user_data
    
    for update_data in updates:
        name = update_data["name"]
        if name in result_data:
            for k, v in update_data.items():
                print(f"{k}: {v}")
                if k != "name":
                    if k in result_data[name]:
                        result_data[name][k] = max(result_data[name][k], v)
                    else:
                        result_data[name][k] = v


print('result', result_data)

# with open(workdir + updates_file, "r", encoding="UTF-8") as upd_f:
    
    # for user in updates:
    #     name = user.get("name")
    #     # print(name)
    #     existing_found = False
    #     for existing_user in data:
    #         # print(existing_user["name"])
    #         if existing_user["name"] == name:
    #             # print("good")
    #             existing_found = True
    #             result_data[name] = existing_user.copy()
    #             del result_data[name]["name"]

    #             for k, v in user.items():
    #                 if k != "name":
    #                     if k in result_data[name]:
    #                         result_data[name][k] = max(result_data[name][k], v)
    #                     else:
    #                         result_data[name][k] = v

with open(workdir + in_file + "_out", "w", encoding="UTF-8") as out_file:
    json.dump(result_data, out_file, ensure_ascii=False)

print(result_data)
            
