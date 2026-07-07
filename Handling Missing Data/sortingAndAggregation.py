import pandas as pd

data = {
    "Employee": ["Mohit", "Rahul", "Aman", "Priya", "Neha", "Rohit", "Sneha", "Ankit"],
    "Age": [22, 25, 24, 28, 26, 30, 27, 23],
    "Salary": [35000, 42000, 38000, 50000, 47000, 62000, 54000, 39000],
    "Performance Score": [85, 92, 78, 95, 88, 80, 91, 84]
}

df = pd.DataFrame(data)

# print(df)
#sort by one column
# print(df.sort_values("Salary"))

# print(df.sort_values("Salary", ascending=False))



#sort by Multiple Columns

# print(
#     df.sort_values(
#         by=["Age","Salary"]
#     )
# )

df.sort_values(
    by=["Age", "Salary"],
    ascending=[True, False],
    inplace=True
)

print(df)



import pandas as pd

# =====================================================
# CREATE DATAFRAME
# =====================================================

data = {
    "Employee": ["Mohit", "Rahul", "Aman", "Priya", "Neha", "Rohit", "Sneha", "Ankit"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Marketing", "Finance"],
    "Age": [22, 25, 25, 28, 26, 30, 27, 25],
    "Salary": [35000, 42000, 38000, 50000, 47000, 62000, 54000, 39000],
    "Performance Score": [85, 92, 78, 95, 88, 80, 91, 84]
}

df = pd.DataFrame(data)

print("="*70)
print("Original DataFrame")
print("="*70)
print(df)

# =====================================================
# SORTING
# =====================================================

# -----------------------------------------------------
# 1. Sort by Salary (Ascending)
# -----------------------------------------------------

print("\n1. Sort Salary (Ascending)")
print(df.sort_values(by="Salary"))

# -----------------------------------------------------
# 2. Sort by Salary (Descending)
# -----------------------------------------------------

print("\n2. Sort Salary (Descending)")
print(df.sort_values(by="Salary", ascending=False))

# -----------------------------------------------------
# 3. Sort by Age
# -----------------------------------------------------

print("\n3. Sort by Age")
print(df.sort_values(by="Age"))

# -----------------------------------------------------
# 4. Sort by Multiple Columns
# -----------------------------------------------------
# First sort by Age.
# If Age is same then sort Salary in descending order.

print("\n4. Sort by Age and Salary")

print(
    df.sort_values(
        by=["Age", "Salary"],
        ascending=[True, False]
    )
)

# -----------------------------------------------------
# 5. Sort by Index
# -----------------------------------------------------

print("\n5. Sort by Index")
print(df.sort_index())

# -----------------------------------------------------
# 6. Sort Index Descending
# -----------------------------------------------------

print("\n6. Sort Index Descending")
print(df.sort_index(ascending=False))

# =====================================================
# AGGREGATION
# =====================================================

# -----------------------------------------------------
# 7. Count
# -----------------------------------------------------

print("\n7. Count")
print(df["Salary"].count())

# -----------------------------------------------------
# 8. Sum
# -----------------------------------------------------

print("\n8. Sum")
print(df["Salary"].sum())

# -----------------------------------------------------
# 9. Mean
# -----------------------------------------------------

print("\n9. Mean")
print(df["Salary"].mean())

# -----------------------------------------------------
# 10. Median
# -----------------------------------------------------

print("\n10. Median")
print(df["Salary"].median())

# -----------------------------------------------------
# 11. Mode
# -----------------------------------------------------

print("\n11. Mode")
print(df["Department"].mode())

# -----------------------------------------------------
# 12. Minimum
# -----------------------------------------------------

print("\n12. Minimum Salary")
print(df["Salary"].min())

# -----------------------------------------------------
# 13. Maximum
# -----------------------------------------------------

print("\n13. Maximum Salary")
print(df["Salary"].max())

# -----------------------------------------------------
# 14. Standard Deviation
# -----------------------------------------------------

print("\n14. Standard Deviation")
print(df["Salary"].std())

# -----------------------------------------------------
# 15. Variance
# -----------------------------------------------------

print("\n15. Variance")
print(df["Salary"].var())

# -----------------------------------------------------
# 16. Multiple Aggregation
# -----------------------------------------------------

print("\n16. Multiple Aggregation")

print(
    df["Salary"].agg(
        [
            "count",
            "sum",
            "mean",
            "median",
            "min",
            "max",
            "std",
            "var"
        ]
    )
)

# -----------------------------------------------------
# 17. Aggregation on Multiple Columns
# -----------------------------------------------------

print("\n17. Multiple Columns Aggregation")

print(
    df[["Age", "Salary", "Performance Score"]].agg(
        [
            "mean",
            "min",
            "max",
            "median"
        ]
    )
)

print("\nProgram Completed Successfully.")