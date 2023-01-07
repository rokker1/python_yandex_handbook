import numpy as np
import pandas as pd
import os

students = pd.read_csv(os.path.join("6.Math", "2.pandas", "Students_Performance_132b1e1ff9.csv"))
print(students.head())
print(students[10:13])

print(students[students["test preparation course"] == "completed"][["math score"]].head())

with_course = students[students["test preparation course"] == "completed"]
print(with_course[[
                        "math score",
                        "reading score",
                        "writing score"
                    ]].sort_values([
                                    "math score",
                                    "reading score",
                                    "writing score"
                                ], ascending=False).head())

with_course = students[students["test preparation course"] == "completed"]
students["total score"] = students["math score"] + students["reading score"] + students["writing score"]
print(students.sort_values(["total score"], ascending=False).head())

scores = students.assign(total_score=lambda x: x["math score"] + x["reading score"] + x["writing score"])
print(scores.sort_values(["total_score"], ascending=False).head())

