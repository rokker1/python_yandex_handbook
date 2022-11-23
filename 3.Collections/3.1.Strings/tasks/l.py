N = int(input())
meals = [
    "Манная",
    "Гречневая",
    "Пшённая",
    "Овсяная",
    "Рисовая"
]
menu = N * meals
for i in range(N):
    print(menu[i])