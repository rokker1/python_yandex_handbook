def add_value(x, list_arg=None):
    if list_arg is None:
        list_arg = []
    list_arg += [x]
    return list_arg


print(add_value(0))
print(add_value(0, [1, 2, 3]))
print(add_value(1))
print(add_value(2))

def final_price(price, discount=1):
    return price - price * discount / 100


print(final_price(1000, discount=5))
print(final_price(discount=10, price=1000))