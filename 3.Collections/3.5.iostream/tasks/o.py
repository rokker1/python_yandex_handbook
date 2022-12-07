from sys import stdin
import json

user_input = [line.rstrip("\n") for line in stdin.readlines()]

workdir = "/source/python_yandex_handbook/3.Collections/3.5.iostream/tasks/"
overall_result = 0
with open(workdir + "scoring.json", "r", encoding="UTF-8") as f:
    test_groups = json.load(f)
    i = 0
    for test_group in test_groups:
        weight = int(test_group['points'] / len(test_group['tests']))
        for test in test_group['tests']:
            if test['pattern'] == user_input[i]:
                overall_result += weight
            i += 1

print(overall_result)