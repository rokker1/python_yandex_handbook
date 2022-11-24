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
        output.append(a / b)
    

print(output[0])