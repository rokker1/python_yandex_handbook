characters = {}
while (line := "".join(input().split())) != "ФИНИШ":
    for c in line:
        characters[c.lower()] = characters.get(c.lower(), 0) + 1
pairs = dict({(v, k) for k, v in characters.items()})
max_freq = max(pairs.keys())
chars = []
for item in pairs.items():
    if item[0] == max_freq:
        chars.append(item[1])
print(sorted(chars)[0])