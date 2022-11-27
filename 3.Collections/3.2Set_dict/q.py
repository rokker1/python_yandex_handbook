db = {}
db_2 = {}
while (line := input()) != "":
    friends = line.split()
    if not db.get(friends[0]):
        db[friends[0]] = [friends[1]]
    else:
        db[friends[0]].append(friends[1])
    if not db_2.get(friends[1]):
        db_2[friends[1]] = [friends[0]]
    else:
        db_2[friends[1]].append(friends[0])

print(db)
print(db_2)

for person, first_friends in db.items():
    second_friends = set()
    for first_friend in first_friends:
        if first_friend in db:
            for second_friend in db[first_friend]:
                second_friends.add(second_friend)

        for second_friend in db_2[first_friend]:
            second_friends.add(second_friend)
    print(person, second_friends)