import math
operands = input().split()
output = []
for i, c in enumerate(operands):
    
    if c.isdigit():
        output.append(int(c))
    elif c == '-':
        b = output.pop()
        a = output.pop()
        output.append(a - b)
    elif c == '+':
        b = output.pop()
        a = output.pop()
        output.append(a + b)
    elif c == '*':
        b = output.pop()
        a = output.pop()
        output.append(a * b)
    elif c == '/':
        b = output.pop()
        a = output.pop()
        output.append(a // b)
    elif c == '~':
        a = output.pop()
        output.append(-a)
    elif c == '!':
        a = output.pop()
        output.append(math.factorial(a))
    elif c == '#':
        a = output.pop()
        output.append(a)
        output.append(a)   
    elif c == '@':
        c = output.pop()
        b = output.pop()
        a = output.pop()
        output.append(b)
        output.append(c)
        output.append(a)
print(output[0])