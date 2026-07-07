
import pandas as pd

# =====================================================
# CREATE DATAFRAME
# =====================================================

data = {
    "Employee": ["Mohit", "Rahul", "Aman", "Priya", "Neha", "Rohit", "Sneha", "Ankit"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Marketing", "Finance"],
    "Age": [22, 25, 24, 28, 26, 30, 27, 23],
    "Salary": [35000, 42000, 38000, 50000, 47000, 62000, 54000, 39000],
    "Performance Score": [85, 92, 78, 95, 88, 80, 91, 84]
}

df = pd.DataFrame(data)

print("=" * 60)
print("Original DataFrame")
print("=" * 60)
print(df)

# =====================================================
# 1. GROUP BY DEPARTMENT
# =====================================================

print("\n1. Group by Department")

print(df.groupby("Department"))

# =====================================================
# 2. MEAN SALARY OF EACH DEPARTMENT
# =====================================================

print("\n2. Average Salary of Each Department")

print(df.groupby("Department")["Salary"].mean())

# =====================================================
# 3. TOTAL SALARY OF EACH DEPARTMENT
# =====================================================

print("\n3. Total Salary of Each Department")

print(df.groupby("Department")["Salary"].sum())

# =====================================================
# 4. MAXIMUM SALARY
# =====================================================

print("\n4. Maximum Salary")

print(df.groupby("Department")["Salary"].max())

# =====================================================
# 5. MINIMUM SALARY
# =====================================================

print("\n5. Minimum Salary")

print(df.groupby("Department")["Salary"].min())

# =====================================================
# 6. NUMBER OF EMPLOYEES
# =====================================================

print("\n6. Employee Count")

print(df.groupby("Department")["Employee"].count())

# =====================================================
# 7. MULTIPLE AGGREGATION
# =====================================================

print("\n7. Multiple Aggregation")

print(

    df.groupby("Department")["Salary"].agg(

        ["count", "sum", "mean", "min", "max", "median"]

    )

)

# =====================================================
# 8. MULTIPLE COLUMNS
# =====================================================

print("\n8. Salary and Performance Score")

print(

    df.groupby("Department")[

        ["Salary", "Performance Score"]

    ].mean()

)

# =====================================================
# 9. GROUP BY TWO COLUMNS
# =====================================================

print("\n9. Department and Age")

print(

    df.groupby(

        ["Department", "Age"]

    )["Salary"].mean()

)

# =====================================================
# 10. RESET INDEX
# =====================================================

print("\n10. Reset Index")

print(

    df.groupby("Department")["Salary"]

    .mean()

    .reset_index()

)