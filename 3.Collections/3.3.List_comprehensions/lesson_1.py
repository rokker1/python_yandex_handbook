from sys import getsizeof

# iterator
numbers = (int(input()) for i in range(5))
print(numbers)

# Create iterator from a 1 mln integer numbers
numbers_iter = (i for i in range(10 ** 6))
# Выводим количество байт, занятых итератором
print(f"Iterator size is: {getsizeof(numbers_iter)} bytes.")

# Create a list
numbers_list = list(range(10 ** 6))
print(f"List size is {getsizeof(numbers_list)} bytes.")

from timeit import timeit

# print(round(timeit("s = '; '.join(str(x) for x in range(10 ** 7))", number=10), 3))
# print(round(timeit("s = '; '.join([str(x) for x in list(range(10 ** 7))])", number=10), 3))


x = 5
print(id(x))
x = 10
print(id(x))

x = 1
y = x
print(id(x))
print(id(y))
print(x is y)

x = [el ** 2 for el in range(5)]
y = [el ** 2 for el in range(5)]
print(x == y)
print(x is y)

numbers = [1, 2, 3]
print(f"{numbers}, id = {id(numbers)}")
numbers += [4]
print(f"{numbers}, id = {id(numbers)}")


numbers = [1, 2, 3]
print(f"{numbers}, id = {id(numbers)}")
numbers = numbers + [4]
print(f"{numbers}, id = {id(numbers)}")

x = [1, 2, 3]
y = x
print(x is y)
x[0] = 0
print(x)
print(y)
print(x is y)

# копия с помощью среза
x = [1, 2, 3]
y = x[:]
print(x is y)
x[0] = 0
print(x)
print(y)
print(x is y)

print("numbers example")
numbers = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
numbers_copy = numbers[:] #copy
print([numbers_copy[i] is numbers[i] for i in range(len(numbers))])

numbers2 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
munbers2_copy = [elem[:] for elem in numbers] # deepcopy
print([numbers2[i] is numbers_copy[i] for i in range(len(numbers2))])