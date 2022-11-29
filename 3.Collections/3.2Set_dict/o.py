def decimalToBinary(n):
    s = bin(int(n))
    return s.removeprefix("0b")


answer = []
input_numbers = input().split()
for input_number in input_numbers:
    binary = decimalToBinary(input_number)
    digit_info = {
        "digits": len(binary),
        "units": 0,
        "zeros": 0
    }
    
    for char in binary:
        if char == "0":
            digit_info["zeros"] = digit_info["zeros"] + 1
        elif char == "1":
            digit_info["units"] = digit_info["units"] + 1

    answer.append(digit_info)

print(answer)