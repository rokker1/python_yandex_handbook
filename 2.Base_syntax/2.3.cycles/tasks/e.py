s = 0.0
while (p := float(input())) != 0:
    if p >= 500:
        s += (p * 0.9)
    else:
        s += p
print(s)