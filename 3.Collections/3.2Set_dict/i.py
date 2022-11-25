information = {}


while (line := input()) != "":
    objects = line.split()
    for object in objects:
        information[object] = 1 + information.get(object, 0)

for k, v in information.items():
    print(f"{k} {v}")