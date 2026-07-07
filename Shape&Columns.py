'''
1-how big is your dataset
2- what are the names of columns

shape and columns
'''

import pandas as pd

data = {
    "Employee": ["Mohit", "Rahul", "Aman", "Priya", "Neha", "Rohit", "Sneha", "Ankit"],
    "Age": [22, 25, 24, 28, 26, 30, 27, 23],
    "Salary": [35000, 42000, 38000, 50000, 47000, 62000, 54000, 39000],
    "Performance Score": [85, 92, 78, 95, 88, 80, 91, 84]
}

df = pd.DataFrame(data)
print(df)

print(f'shape: {df.shape}')
print(f'Columns Name: {df.columns}')