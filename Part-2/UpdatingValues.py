import pandas as pd

# =====================================================
# CREATE DATAFRAME
# =====================================================

data = {
    "Employee": ["Mohit", "Rahul", "Aman", "Priya", "Neha", "Rohit", "Sneha", "Ankit"],
    "Age": [22, 25, 24, 28, 26, 30, 27, 23],
    "Salary": [35000, 42000, 38000, 50000, 47000, 62000, 54000, 39000],
    "Performance Score": [85, 92, 78, 95, 88, 80, 91, 84]
}

df = pd.DataFrame(data)
print(df)

#.loc[]
# df.loc[row_index, "column name"] = new_value

# df.loc[0, "Salary"] =55000
# print(df)

############
#increasing salary by 5 percent 
df['Salary'] = df['Salary']*1.05
print(df)


# # =====================================================
# # CREATE DATAFRAME
# # =====================================================

# data = {
#     "Employee": ["Mohit", "Rahul", "Aman", "Priya", "Neha", "Rohit", "Sneha", "Ankit"],
#     "Age": [22, 25, 24, 28, 26, 30, 27, 23],
#     "Salary": [35000, 42000, 38000, 50000, 47000, 62000, 54000, 39000],
#     "Performance Score": [85, 92, 78, 95, 88, 80, 91, 84]
# }

# df = pd.DataFrame(data)

# print("=" * 60)
# print("Original DataFrame")
# print("=" * 60)
# print(df)

# # =====================================================
# # 1. UPDATE SINGLE CELL USING loc[]
# # =====================================================

# # Change Rahul's salary from 42000 to 45000
# df.loc[1, "Salary"] = 45000

# print("\n1. Updated Rahul's Salary")
# print(df)

# # =====================================================
# # 2. UPDATE MULTIPLE COLUMNS OF A ROW
# # =====================================================

# # Change Aman's age and salary
# df.loc[2, ["Age", "Salary"]] = [25, 40000]

# print("\n2. Updated Aman's Age and Salary")
# print(df)

# # =====================================================
# # 3. UPDATE ENTIRE COLUMN
# # =====================================================

# # Increase everyone's salary by 5000
# df["Salary"] = df["Salary"] + 5000

# print("\n3. Increased Everyone's Salary")
# print(df)

# # =====================================================
# # 4. UPDATE USING CONDITION
# # =====================================================

# # Give employees with salary > 50000 a bonus
# df.loc[df["Salary"] > 50000, "Bonus"] = 5000

# print("\n4. Bonus for Salary > 50000")
# print(df)

# # =====================================================
# # 5. UPDATE USING MULTIPLE CONDITIONS
# # =====================================================

# # Excellent performers get promotion
# df.loc[
#     (df["Performance Score"] >= 90) &
#     (df["Salary"] > 45000),
#     "Promotion"
# ] = "Yes"

# print("\n5. Promotion Column")
# print(df)

# # =====================================================
# # 6. UPDATE REMAINING VALUES
# # =====================================================

# # Everyone else gets No
# df["Promotion"] = df["Promotion"].fillna("No")

# print("\n6. Fill Remaining Promotion Values")
# print(df)

# # =====================================================
# # 7. UPDATE TEXT VALUES
# # =====================================================

# # Change Mohit to Mohit Shrivastav
# df.loc[df["Employee"] == "Mohit", "Employee"] = "Mohit Shrivastav"

# print("\n7. Updated Employee Name")
# print(df)

# # =====================================================
# # 8. UPDATE WHOLE COLUMN USING apply()
# # =====================================================

# # Convert employee names to uppercase
# df["Employee"] = df["Employee"].apply(str.upper)

# print("\n8. Uppercase Employee Names")
# print(df)

# # =====================================================
# # 9. UPDATE USING map()
# # =====================================================

# # Convert Yes/No to Approved/Rejected
# status = {
#     "Yes": "Approved",
#     "No": "Rejected"
# }

# df["Promotion"] = df["Promotion"].map(status)

# print("\n9. Updated Promotion Status")
# print(df)

# # =====================================================
# # 10. UPDATE USING lambda
# # =====================================================

# # Increase salary by 10%
# df["Salary"] = df["Salary"].apply(lambda x: x * 1.10)

# print("\n10. Salary Increased by 10%")
# print(df)

# # =====================================================
# # 11. UPDATE USING np.where()
# # =====================================================

# import numpy as np

# df["Grade"] = np.where(
#     df["Performance Score"] >= 90,
#     "A",
#     "B"
# )

# print("\n11. Grade Column")
# print(df)

# # =====================================================
# # 12. REPLACE VALUES
# # =====================================================

# # Replace Grade B with Average
# df["Grade"] = df["Grade"].replace("B", "Average")

# print("\n12. Replace Grade")
# print(df)

# # =====================================================
# # FINAL DATAFRAME
# # =====================================================

# print("\nFinal DataFrame")
# print(df)