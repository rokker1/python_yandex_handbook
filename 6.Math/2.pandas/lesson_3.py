import numpy as np
import pandas as pd
import os

students = pd.read_csv(os.path.join("6.Math", "2.pandas", "Students_Performance_132b1e1ff9.csv"))
print(students.groupby(["gender", "test preparation course"])["writing score"].count())
