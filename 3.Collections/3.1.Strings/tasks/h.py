N = int(input())
for i in range(N):
    line = input()
    position = line.find("зайка")
    if position != -1:
        print(position + 1)
    else:
        print("Заек нет =(")