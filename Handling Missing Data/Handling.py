#dropna()
import pandas as pd
import numpy as np

data = {
    "Employee": ["Mohit", "Rahul", "Aman", "Priya", "Neha", "Rohit", "Sneha", "Ankit"],
    "Age": [22, 25, np.nan, 28, 26, 30, np.nan, 23],
    "Salary": [35000, np.nan, 38000, 50000, 47000, 62000, 54000, np.nan],
    "Department": ["IT", "HR", "IT", "Finance", np.nan, "IT", "Marketing", "Finance"],
    "Performance Score": [85, 92, 78, np.nan, 88, 80, 91, np.nan]
}

df = pd.DataFrame(data)

print(df)

df.dropna(inplace = True) #delete all rows containing NaN values
print(df)
