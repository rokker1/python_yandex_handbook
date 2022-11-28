numbers = {1, 2, 3, 4, 5}
my_dict = {
    n: [delimeter for delimeter in range(1, n + 1) if n % delimeter == 0] for n in numbers 
}
print(my_dict)