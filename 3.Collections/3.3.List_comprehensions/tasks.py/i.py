numbers = [1, 1, 3, 1, 10, 2, 4, 6, 7, 1, 2, 7]

my_string = " - ".join([str(c) for c in sorted(set(numbers))])
print(my_string)