good = input()
cost = int(input())
weight = int(input())
price = cost * weight
money = int(input())

print("Чек")
print(good, ' - ', weight, 'кг - ', cost, 'руб/кг', sep="")
print(f"Итого: {price}руб")
print(f"Внесено: {money}руб")
print(f"Сдача: {int(money - price)}руб")