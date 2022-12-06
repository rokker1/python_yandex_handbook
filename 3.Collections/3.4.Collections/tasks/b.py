kids = input().split(sep=", ")
second_kids = input().split(sep=", ")
pairs = zip(kids, second_kids)
for k1, k2 in pairs:
    print(f"{k1} - {k2}")