line = input()
numbers = line.split()
P = int(input())
result = [int(i) ** P for i in numbers]

result_string = ""
for i in result:
    result_string += str(i)
    result_string += " "
print(result_string)