import itertools

print(itertools.product("ABCD", repeat=4))

'''
Функции, возвращающие бесконечные итераторы
'''
# count(start, step)
from itertools import count
for value in count(0, 0.1):
    if value <= 1:
        print(round(value, 1))
    else:
        break

# cycle(iterable)
from itertools import cycle

max_len = 10
s = ""
for letter in cycle("ABC"):
    if len(s) < 10:
        s += letter
    else:
        break
print(s)

#repeat(object, times)
from itertools import repeat
result = list(repeat("ABC", 5))
print(result)

'''
Функции, выполняющиеся до кратчайшей входной последовательности
'''

# accumulate
from itertools import accumulate

for value in accumulate([1, 2, 3, 4, 5]):
    print(value)

# chain
from itertools import chain

values = list(chain("АБВ", "ГДЕЁ", "ЖЗИЙК"))
print(values)
values = list(chain.from_iterable(["АБВ", "ГДЕЁ", "ЖЗИЙК"]))
print(values)

'''
Функции для комбинаторики
'''
# product
from itertools import product

values = list(product([1, 2, 3], "АБВГ"))
print(values)

#permutations
from itertools import permutations

values = list(permutations("АБВ"))
print(values)

# combinations 
from itertools import combinations, combinations_with_replacement

values = list(combinations("АБВ", 2))
print(values)
values = list(combinations_with_replacement("ABC", 2))
print(values)

# enumarate
for index, value in enumerate("ABC", 1):
    print(index, value)


# zip
print(list(zip("ABC", [1, 2, 3])))
