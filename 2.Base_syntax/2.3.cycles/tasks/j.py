x = 0
y = 0

while (cmd := input()) != 'СТОП':
    distance = int(input())
    match cmd:
        case "СЕВЕР":
            y += distance
        case "ЮГ":
            y -= distance
        case "ВОСТОК":
            x += distance
        case "ЗАПАД":
            x -= distance
        case _:
            print("wrong cmd")

print(y)
print(x)