from sys import stdin
from statistics import mean
import json 

args = stdin.readlines()
args = [string.rstrip("\n") for string in args]

numbers = []
filename = args[0]
with open(filename, "r", encoding="UTF-8") as input_file:
    for line in input_file:
        numbers.extend([int(x) for x in line.rstrip('\n').split()])

statistics = {
    "count": len(numbers),
    "positive_count": len([number for number in numbers if number > 0]),
    "min": min(numbers),
    "max": max(numbers),
    "sum": sum(numbers),
    "average": round(mean(numbers), 2)
}

with open(args[1], "w", encoding="UTF-8") as out_json:
    json.dump(statistics, out_json, ensure_ascii=False, )