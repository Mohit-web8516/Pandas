import pandas as pd

# ----------------------------------
# DataFrame 1
# ----------------------------------

df1 = pd.DataFrame({
    "Employee": ["Mohit", "Rahul", "Aman"],
    "Salary": [35000, 42000, 38000]
})

# ----------------------------------
# DataFrame 2
# ----------------------------------

df2 = pd.DataFrame({
    "Employee": ["Priya", "Neha", "Rohit"],
    "Salary": [50000, 47000, 62000]
})

print("DataFrame 1")
print(df1)

print("\nDataFrame 2")
print(df2)

# ----------------------------------
# Row-wise Concatenation
# ----------------------------------

print("\nRow-wise Concatenation")
print(pd.concat([df1, df2]))

# ----------------------------------
# Row-wise with New Index
# ----------------------------------

print("\nIgnore Index")
print(pd.concat([df1, df2], ignore_index=True))

# ----------------------------------
# Column-wise Concatenation
# ----------------------------------

employee = pd.DataFrame({
    "Employee": ["Mohit", "Rahul", "Aman"]
})

salary = pd.DataFrame({
    "Salary": [35000, 42000, 38000]
})

print("\nColumn-wise Concatenation")
print(pd.concat([employee, salary], axis=1))

# ----------------------------------
# Different Columns
# ----------------------------------

df3 = pd.DataFrame({
    "Employee": ["Sneha", "Ankit"],
    "Age": [27, 23]
})

print("\nDifferent Columns")
print(pd.concat([df1, df3], ignore_index=True))

# ----------------------------------
# Keys
# ----------------------------------

print("\nKeys Example")
print(pd.concat([df1, df2], keys=["Old Employees", "New Employees"]))