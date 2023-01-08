import pandas as pd


def cheque(pricelist, **goods):
    product = []
    price = []
    number = []
    cost = []
    for good, count in goods.items():
        product.append(good)
        price.append(pricelist[good])
        number.append(count)
        cost.append(count * pricelist[good])
    
    df = pd.DataFrame({
        "product": product,
        "price": price,
        "number": number,
        "cost": cost
    }).sort_values("product")
    df.index = pd.RangeIndex(0, len(df.index), 1)
    return df


products = ['bread', 'milk', 'soda', 'cream']
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)
result = cheque(price_list, soda=3, milk=2, cream=1)
print(result)

