def final_price(*prices, discount=1):
    return [price - price * discount / 100 for price in prices]


print(final_price(100, 200, 300, discount=5))