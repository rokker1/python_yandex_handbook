n = int(input())
first = ""
for i in range(n):
    player = input()
    if first == "" or player < first:
        first = player
print(first)
    