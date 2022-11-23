m = int(input())
n = int(input())
row = 0
for i in range(m):
    line = ""
    first = True
    row = row + 1
    column = row
    for j in range(n):
        if not first:
            line += " "
        first = False
        line += str(column)
        column += n
        
    print(line)