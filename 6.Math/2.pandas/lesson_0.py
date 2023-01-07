import numpy as np
import pandas as pd

data = np.arange(5)
index = ["a", "b", "c", "d", "e"]
s = pd.Series(data, index)
print(s)
print()
s = pd.Series(np.linspace(0, 1, 5))
print(s)

d = {"a": 10, "b": 20, "c": 30, "g": 40}
print(pd.Series(d))
print()
print(pd.Series(d, index=["a", "b", "c", "d", "e", "f", "g", "h"]))

index = ["a", "b", "c"]
print(pd.Series(5, index=index))

data = np.arange(5)
index = ["a", "b", "c", "d", "e"]
s = pd.Series(data, index)
print("Выбор одного элемента")
print(s["a"])
print("Выбор нескольких элементов")
print(s[["a", "b"]])
print("Срез")
print(s[1:])
print("Поэлементное сложение")
print(s + s)
print("Фильтрация")
print(s[s > 2])
s.name = "Данные"
s.index.name = "Индекс"
print(s)

