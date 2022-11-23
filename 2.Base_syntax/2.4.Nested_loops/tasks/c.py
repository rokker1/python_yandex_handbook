size = int(input())
c = 1
while size > 0:
    current_line = ""
    for i in range(1, size):
        current_line += str(i)
        current_line += " "
        print(current_line)
    size -= c
    c += 1
    