a = input()
b = input()
c = input()

pattern = "зайка"

a_has_pattern = pattern in a
b_has_pattern = pattern in b
c_has_pattern = pattern in c

answer = ""
length = 0

if pattern in a:
    answer = a
    length = len(a)

if pattern in b:
    if answer == "":
        answer = b
        length = len(b)
    elif b < answer:
        answer = b
        length = len(b)

if pattern in c:
    if answer == "":
        answer = c
        length = len(c)
    elif c < answer:
        answer = c
        length = len(c)

print(answer, length)