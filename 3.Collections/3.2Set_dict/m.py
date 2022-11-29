N = int(input())
available_food = set()

for i in range(N):
    available_food.add(input())
days_info_count = int(input())
for i in range(days_info_count):
    daily_food_info_count = int(input())
    todays_menu = set()
    for j in range(daily_food_info_count):
        todays_menu.add(input())
    available_food.difference_update(todays_menu)
for food in sorted(available_food):
    print(food)
if not available_food:
    print("Готовить нечего")