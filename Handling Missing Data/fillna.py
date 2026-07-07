import pandas as pd

data = {
    "Employee": ["Mohit", "Rahul", "Aman", "Priya", "Neha", "Rohit", "Sneha", "Ankit"],
    "Age": [22, 25, None, 28, 26, 30, None, 23],
    "Salary": [35000, None, 38000, 50000, 47000, 62000, 54000, None],
    "Department": ["IT", "HR", "IT", "Finance", None, "IT", "Marketing", "Finance"],
    "Performance Score": [85, 92, 78, None, 88, 80, 91, None]
}

df = pd.DataFrame(data)

print(df)

#Fill every missing value

# filled_df = df.fillna(0)

# print(filled_df)

## Fill Using Mean 

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())


print(df)