flag = False
for i in range(26):
    for j in range(26):
        text = f"{chr(ord('a') + i)}{chr(ord('a') + j)}"
        if text == 'ya':
            print(text)
            flag = True
            break
    if flag:
        break

password = "right_password"
while True:
    if input("enter the password:") == password:
        print('Пароль принимается')
        break

while (text := input("enter string 'STOP for stop'")) != 'STOP for stop':
    if text == 'ignore_else':
        break
else:
    print("Cycle stopped")