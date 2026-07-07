import pandas as pd

# ============================================================
# CREATE SAMPLE DATAFRAME
# ============================================================

# Dictionary containing employee information
data = {
    "Employee": ["Mohit", "Rahul", "Aman", "Priya", "Neha", "Rohit", "Sneha", "Ankit"],
    "Age": [22, 25, 24, 28, 26, 30, 27, 23],
    "Salary": [35000, 42000, 38000, 50000, 47000, 62000, 54000, 39000],
    "Performance Score": [85, 92, 78, 95, 88, 80, 91, 84]
}

# Convert dictionary into a DataFrame
df = pd.DataFrame(data)

# Print original DataFrame
print("=" * 60)
print("Original DataFrame")
print("=" * 60)
print(df)


# ============================================================
# 1. SELECT A SINGLE COLUMN
# ============================================================

# Select only the Employee column.
# Returns a Series (1-dimensional)
print("\n1. Employee Column")
employee = df["Employee"]
print(employee)


# Select only the Salary column.
# Returns a Series
print("\n2. Salary Column")
salary = df["Salary"]
print(salary)


# Select only the Age column.
print("\n3. Age Column")
age = df["Age"]
print(age)


# Select only the Performance Score column.
print("\n4. Performance Score Column")
performance = df["Performance Score"]
print(performance)


# ============================================================
# 2. SELECT A SINGLE COLUMN AS A DATAFRAME
# ============================================================

# Double square brackets create a DataFrame instead of a Series.
print("\n5. Salary Column as DataFrame")
salary_df = df[["Salary"]]
print(salary_df)


# ============================================================
# 3. SELECT MULTIPLE COLUMNS
# ============================================================

# Select Employee and Salary columns.
# Returns a DataFrame
print("\n6. Employee and Salary")
subset = df[["Employee", "Salary"]]
print(subset)


# Select Employee and Age
print("\n7. Employee and Age")
subset = df[["Employee", "Age"]]
print(subset)


# Select Employee, Salary and Performance Score
print("\n8. Employee, Salary and Performance Score")
subset = df[["Employee", "Salary", "Performance Score"]]
print(subset)


# Select only numeric columns manually
print("\n9. Numeric Columns")
subset = df[["Age", "Salary", "Performance Score"]]
print(subset)


# ============================================================
# 4. SELECT COLUMNS IN DIFFERENT ORDER
# ============================================================

# Pandas displays columns in the order you specify.
print("\n10. Custom Column Order")
subset = df[["Salary", "Employee", "Age"]]
print(subset)


# ============================================================
# 5. SELECT COLUMNS USING loc[]
# ============================================================

# loc[row_selection, column_selection]
# ':' means select ALL rows
print("\n11. Using loc() - Employee and Salary")
subset = df.loc[:, ["Employee", "Salary"]]
print(subset)


# Select only Salary column using loc()
print("\n12. Using loc() - Salary")
subset = df.loc[:, ["Salary"]]
print(subset)


# Select Employee, Age and Performance Score
print("\n13. Using loc() - Employee, Age, Performance Score")
subset = df.loc[:, ["Employee", "Age", "Performance Score"]]
print(subset)


# ============================================================
# 6. SELECT COLUMNS USING iloc[]
# ============================================================

# iloc uses COLUMN POSITIONS instead of column names.
# Syntax:
# df.iloc[row_position, column_position]

print("\n14. Using iloc() - First Column")
subset = df.iloc[:, 0]
print(subset)


print("\n15. Using iloc() - First Column as DataFrame")
subset = df.iloc[:, [0]]
print(subset)


print("\n16. Using iloc() - First Two Columns")
subset = df.iloc[:, 0:2]
print(subset)


print("\n17. Using iloc() - Second and Fourth Columns")
subset = df.iloc[:, [1, 3]]
print(subset)


# ============================================================
# 7. SELECT LAST COLUMN
#============================================================

# -1 means the last column.
print("\n18. Last Column")
subset = df.iloc[:, -1]
print(subset)


# ============================================================
# 8. SELECT FIRST THREE COLUMNS
# ============================================================

print("\n19. First Three Columns")
subset = df.iloc[:, :3]
print(subset)


# ============================================================
# 9. SELECT LAST TWO COLUMNS
# ============================================================

print("\n20. Last Two Columns")
subset = df.iloc[:, -2:]
print(subset)


# ============================================================
# 10. STORE SELECTED COLUMNS INTO NEW DATAFRAME
# ============================================================

print("\n21. Store Selected Columns")
employee_salary = df[["Employee", "Salary"]]
print(employee_salary)


# ============================================================
# 11. DISPLAY COLUMN NAMES
# ============================================================

print("\n22. Column Names")
print(df.columns)


# Convert column names into a normal Python list
print("\n23. Column Names as List")
print(df.columns.tolist())


# ============================================================
# 12. LOOP THROUGH EVERY COLUMN
# ============================================================

print("\n24. Loop Through Columns")

for column in df.columns:
    print(column)


# ============================================================
# 13. PRACTICE EXAMPLES
# ============================================================

# Select Employee and Salary
print("\n25. Practice 1")
print(df[["Employee", "Salary"]])

# Select Salary and Performance Score
print("\n26. Practice 2")
print(df[["Salary", "Performance Score"]])

# Select Employee, Age and Salary
print("\n27. Practice 3")
print(df[["Employee", "Age", "Salary"]])

# Select columns using positions
print("\n28. Practice 4")
print(df.iloc[:, [0, 2]])

# Select columns using loc()
print("\n29. Practice 5")
print(df.loc[:, ["Employee", "Performance Score"]])

print("\n========== END ==========")