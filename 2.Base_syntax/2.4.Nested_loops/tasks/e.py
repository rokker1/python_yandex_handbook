N = int(input())
result = 0
for i in range(0, N):
    found = False
    while (line := input()) != 'ВСЁ':
        if line == 'зайка':
            result += 1
            found = True
            break
    
    if found:
        while (line := input()) != 'ВСЁ':
            pass

print(result)