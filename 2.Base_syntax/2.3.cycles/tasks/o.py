n = int(input())
phrase = "зайка"
count = 0
for i in range(n):
    string = input()
    if phrase in string:
        count += 1
print(count)
