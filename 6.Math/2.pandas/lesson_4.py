import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

students = pd.read_csv(os.path.join("6.Math", "2.pandas", "Students_Performance_132b1e1ff9.csv"))
agg_functions = {
    "math score": ["mean", "median"]
}
print(students.groupby(["gender", 'test preparation course']).agg(agg_functions))

plt.hist(students["math score"], label="Тест по математике", bins=25, stacked=False)
plt.xlabel("Баллы за тест")
plt.ylabel("Количество студентов")
plt.legend()
plt.show()