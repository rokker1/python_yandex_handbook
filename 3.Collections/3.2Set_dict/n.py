N = int(input())
available_food = set()
available_meals = set()
for i in range(N):
    available_food.add(input())
cookbook_meal_count = int(input())
for i in range(cookbook_meal_count):
    meal = input()
    ingridients_count = int(input())
    ingridients = set()
    for j in range(ingridients_count):
        ingridients.add(input())
    if ingridients <= available_food:
        available_meals.add(meal)
if available_meals:
    for meal in sorted(available_meals):
        print(meal)
else:
    print("Готовить нечего")
