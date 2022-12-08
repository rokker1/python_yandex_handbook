from sys import stdin
some_map = {
    " ": "",
    "\n": "",
    "\x20": "",
    "\t": "",
    # "&nbsp;": "",
    # "&nbsp;": ""
}
table = str.maketrans(some_map)
query = stdin.readline().rstrip('\n').translate(table).lower()
filesnames = [line.rstrip('\n') for line in stdin.readlines()]
workdir = "/source/python_yandex_handbook/3.Collections/3.5.iostream/tasks/"

relevant_files = []
for filename in filesnames:
    with open(workdir + filename, 'r', encoding="UTF-8") as f:
        text = f.read().translate(table).lower()
        if query in text:
            relevant_files.append(filename)
for f in relevant_files:
    print(f)
if len(relevant_files) == 0:
    print("404. Not Found")
