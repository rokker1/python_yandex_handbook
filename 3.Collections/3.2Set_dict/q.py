db = {}


def print_second_frineds(sf):
    for person in sorted(sf):
        output_line = f"{person}: "

        if sf[person]:
            first = True
            for second_friend in sorted(sf[person]):
                if not first:
                    output_line += ", "
                first = False
                output_line += second_friend
        print(output_line)


while (line := input()) != "":
    friends = line.split()
    if friends[0] in db:
        db[friends[0]].append(friends[1])
    else:
        db[friends[0]] = [friends[1]]
    if friends[1] in db:
        db[friends[1]].append(friends[0])
    else:
        db[friends[1]] = [friends[0]]

second_friends = {}

for person in db:
    second_friends[person] = set()
    for first_friend in db[person]:
        for second_friend in db[first_friend]:
            if person != second_friend:
                second_friends[person].add(second_friend)
    

print_second_frineds(second_friends)
