import numpy as np
import pandas as pd

students_marks_dict = {
    "student": [
        "Sa", "Sb", "Sb"
    ],
    "math": [5, 4, 3],
    "physics": [4, 5, 5]
}
students = pd.DataFrame(students_marks_dict)
print(students)
print(students.index)
print(students.columns)


students.index = ["A", "B", "C"]
print(students.index)
print(students)

print(students.loc["B":])

print(type(students["student"]))
students.to_excel("wow_thisis_file.xlsx")