n = int(input())


def check_alphabet(n: int):
    a = ord('а')

    flag = True
    for i in range(n):
        s = input()
        if ord(s[0]) == a:
            a += 1
        else:
            flag = False
    if flag:        
        print("YES")
    else:
        print("NO")
    return
        

check_alphabet(n)