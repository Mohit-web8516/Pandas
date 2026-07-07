import pandas as pd

# =====================================================
# CREATE DATAFRAME
# =====================================================

data = {
    "Employee": ["Mohit", "Rahul", "Aman", "Priya", "Neha", "Rohit", "Sneha", "Ankit"],
    "Age": [22, 25, 24, 28, 26, 30, 27, 23],
    "Salary": [35000, 42000, 38000, 50000, 47000, 62000, 54000, 39000],
    "Performance Score": [85, 92, 78, 95, 88, 80, 91, 84],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Marketing", "Finance"],
    "City": ["Delhi", "Mumbai", "Lucknow", "Pune", "Noida", "Bhopal", "Jaipur", "Kanpur"]
}

df = pd.DataFrame(data)

print("=" * 60)
print("Original DataFrame")
print("=" * 60)
print(df)

#df.drop(columns = ["ColumnName"], implace = True)
print("Modified Data")
df.drop(columns= ["Performance Score", "Age"], inplace = True)
print(df)

# =====================================================
# 1. DELETE ONE COLUMN USING drop()
# =====================================================

# drop() returns a NEW DataFrame.
# The original DataFrame remains unchanged.

# new_df = df.drop("City", axis=1)

# print("\n1. Delete City Column")
# print(new_df)

# =====================================================
# 2. DELETE MULTIPLE COLUMNS
# =====================================================

# new_df = df.drop(["Department", "City"], axis=1)

# print("\n2. Delete Department and City")
# print(new_df)

# =====================================================
# 3. DELETE COLUMN PERMANENTLY
# =====================================================

# inplace=True modifies the original DataFrame.

df.drop("Department", axis = 1, inplace=True)

print("\n3. Department Deleted Permanently")
print(df)

# =====================================================
# 4. DELETE COLUMN USING del
# =====================================================

# # del permanently removes the column.

# del df["City"]

# print("\n4. City Deleted using del")
# print(df)

# # =====================================================
# # 5. DELETE COLUMN USING pop()
# # =====================================================

# # Create new DataFrame because Department and City
# # have already been removed.

# data = {
#     "Employee": ["Mohit", "Rahul", "Aman"],
#     "Age": [22, 25, 24],
#     "Salary": [35000, 42000, 38000],
#     "Department": ["IT", "HR", "Finance"]
# }

# df2 = pd.DataFrame(data)

# print("\n5. Original df2")
# print(df2)

# removed_column = df2.pop("Department")

# print("\nAfter pop()")
# print(df2)

# print("\nRemoved Column")
# print(removed_column)

# # =====================================================
# # 6. DELETE COLUMN BY POSITION
# # =====================================================

# # Delete second column (Age)

# column_name = df2.columns[1]

# df2.drop(column_name, axis=1, inplace=True)

# print("\n6. Delete Column by Position")
# print(df2)

# # =====================================================
# # 7. DELETE ALL COLUMNS EXCEPT SOME
# # =====================================================

# data = {
#     "Employee": ["Mohit", "Rahul", "Aman"],
#     "Age": [22, 25, 24],
#     "Salary": [35000, 42000, 38000],
#     "Performance Score": [85, 92, 78]
# }

# df3 = pd.DataFrame(data)

# # Keep only Employee and Salary

# df3 = df3[["Employee", "Salary"]]

# print("\n7. Keep Only Employee and Salary")
# print(df3)

# # =====================================================
# # 8. DELETE COLUMN IF EXISTS
# # =====================================================

# data = {
#     "Employee": ["Mohit", "Rahul"],
#     "Age": [22, 25],
#     "Salary": [35000, 42000]
# }

# df4 = pd.DataFrame(data)

# if "Age" in df4.columns:
#     df4.drop("Age", axis=1, inplace=True)

# print("\n8. Delete Column if Exists")
# print(df4)

# print("\n========== END ==========")