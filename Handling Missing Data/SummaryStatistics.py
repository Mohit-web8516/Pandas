import pandas as pd

data = {
    "Employee": ["Mohit", "Rahul", "Aman", "Priya", "Neha", "Rohit", "Sneha", "Ankit"],
    "Age": [22, 25, 24, 28, 26, 30, 27, 23],
    "Salary": [35000, 42000, 38000, 50000, 47000, 62000, 54000, 39000],
    "Performance Score": [85, 92, 78, 95, 88, 80, 91, 84]
}

df = pd.DataFrame(data)

print(df)



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
# 1. COMPLETE SUMMARY STATISTICS
# =====================================================

# describe() returns summary statistics for all numeric columns.

print("\n1. Complete Summary Statistics")
print(df.describe())

# =====================================================
# 2. SUMMARY OF A SINGLE COLUMN
# =====================================================

print("\n2. Salary Summary")
print(df["Salary"].describe())

# =====================================================
# 3. SUMMARY OF MULTIPLE COLUMNS
# =====================================================

print("\n3. Age and Salary Summary")
print(df[["Age", "Salary"]].describe())

# =====================================================
# 4. SUMMARY OF TEXT COLUMNS
# =====================================================

# include="object" shows summary of string columns.

print("\n4. Text Column Summary")
print(df.describe(include="object"))

# =====================================================
# 5. SUMMARY OF ALL COLUMNS
# =====================================================

# include="all" includes numeric + text columns.

print("\n5. Summary of All Columns")
print(df.describe(include="all"))

# =====================================================
# 6. COUNT
# =====================================================

# Number of non-missing values.

print("\n6. Count")
print(df["Salary"].count())

# =====================================================
# 7. SUM
# =====================================================

# Total salary of all employees.

print("\n7. Sum")
print(df["Salary"].sum())

# =====================================================
# 8. MEAN
# =====================================================

# Average salary.

print("\n8. Mean")
print(df["Salary"].mean())

# =====================================================
# 9. MEDIAN
# =====================================================

# Middle salary after sorting.

print("\n9. Median")
print(df["Salary"].median())

# =====================================================
# 10. MODE
# =====================================================

# Most frequently occurring value.

print("\n10. Mode (Department)")
print(df["Department"].mode())

# =====================================================
# 11. MINIMUM
# =====================================================

print("\n11. Minimum Salary")
print(df["Salary"].min())

# =====================================================
# 12. MAXIMUM
# =====================================================

print("\n12. Maximum Salary")
print(df["Salary"].max())

# =====================================================
# 13. STANDARD DEVIATION
# =====================================================

# Measures how spread out the data is.

print("\n13. Standard Deviation")
print(df["Salary"].std())

# =====================================================
# 14. VARIANCE
# =====================================================

# Square of the standard deviation.

print("\n14. Variance")
print(df["Salary"].var())

# =====================================================
# 15. QUANTILES
# =====================================================

# 25%, 50%, and 75% values.

print("\n15. 25% Quantile")
print(df["Salary"].quantile(0.25))

print("\n16. 50% Quantile (Median)")
print(df["Salary"].quantile(0.50))

print("\n17. 75% Quantile")
print(df["Salary"].quantile(0.75))

# =====================================================
# 16. RANGE
# =====================================================

# Difference between maximum and minimum salary.

salary_range = df["Salary"].max() - df["Salary"].min()

print("\n18. Salary Range")
print(salary_range)

# =====================================================
# 17. MULTIPLE AGGREGATION FUNCTIONS
# =====================================================

print("\n19. Multiple Aggregation on Salary")

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

# =====================================================
# 18. MULTIPLE AGGREGATION ON MULTIPLE COLUMNS
# =====================================================

print("\n20. Multiple Aggregation on Age and Salary")

print(
    df[["Age", "Salary"]].agg(
        [
            "count",
            "mean",
            "min",
            "max",
            "median",
            "std"
        ]
    )
)

# =====================================================
# END
# =====================================================

print("\nSummary Statistics Completed Successfully.")