in_stock = {"coffee": 4, "milk": 4, "cream": 0}
def order(*args):
    cookbook = {
        "Эспрессо": {"coffee": 1, "milk": 0, "cream": 0},
        "Капучино": {"coffee": 1, "milk": 3, "cream": 0},
        "Макиато": {"coffee": 2, "milk": 1, "cream": 0},
        "Кофе по-венски": {"coffee": 1, "milk": 0, "cream": 2},
        "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
        "Кон Панна": {"coffee": 1, "milk": 0, "cream": 1},
    }
    global in_stock
    for beverage in args:

        can_cook = True
        for ingridient, count in cookbook[beverage].items():
            if in_stock[ingridient] < count:
                can_cook = False
                break
        
        if not can_cook:
            continue
        else:
            for ingridient, count in cookbook[beverage].items():
                in_stock[ingridient] -= count
            return beverage
        
    return "К сожалению, не можем предложить Вам напиток"


print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))