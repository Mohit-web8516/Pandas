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

print("="*70)
print("Original DataFrame")
print("="*70)
print(df)

# =====================================================
# COUNT
# =====================================================

print("\nCount")
print(df["Salary"].count())

# =====================================================
# SUM
# =====================================================

print("\nSum")
print(df["Salary"].sum())

# =====================================================
# MEAN
# =====================================================

print("\nMean")
print(df["Salary"].mean())

# =====================================================
# MEDIAN
# =====================================================

print("\nMedian")
print(df["Salary"].median())

# =====================================================
# MODE
# =====================================================

print("\nMode")
print(df["Department"].mode())

# =====================================================
# MINIMUM
# =====================================================

print("\nMinimum Salary")
print(df["Salary"].min())

# =====================================================
# MAXIMUM
# =====================================================

print("\nMaximum Salary")
print(df["Salary"].max())

# =====================================================
# STANDARD DEVIATION
# =====================================================

print("\nStandard Deviation")
print(df["Salary"].std())

# =====================================================
# VARIANCE
# =====================================================

print("\nVariance")
print(df["Salary"].var())

# =====================================================
# QUANTILES
# =====================================================

print("\n25% Quantile")
print(df["Salary"].quantile(0.25))

print("\n50% Quantile")
print(df["Salary"].quantile(0.50))

print("\n75% Quantile")
print(df["Salary"].quantile(0.75))

# =====================================================
# AGG FUNCTION
# =====================================================

print("\nMultiple Aggregation")

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