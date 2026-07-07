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

print("=" * 60)
print("Original DataFrame")
print("=" * 60)
print(df)

###########################
#square brackets df["Column_Name"] = some_Data

df["Bonus"] = df['Salary'] * 0.1
print(df)


#Using insert()

# df.insert(loc, "column_name",some_data)
df.insert(0, "Employee ID ", [10,20,30,40,50,60,70,80])
print(df)


# # =====================================================
# # 1. ADD A COLUMN WITH SAME VALUE
# # =====================================================

# # Every employee belongs to the IT department.

# df["Department"] = "IT"

# print("\n1. Added Department Column")
# print(df)

# # =====================================================
# # 2. ADD A COLUMN USING A LIST
# # =====================================================

# # Each employee belongs to a different city.

# df["City"] = [
#     "Delhi",
#     "Mumbai",
#     "Lucknow",
#     "Pune",
#     "Noida",
#     "Bhopal",
#     "Jaipur",
#     "Kanpur"
# ]

# print("\n2. Added City Column")
# print(df)

# # =====================================================
# # 3. ADD A COLUMN USING CALCULATION
# # =====================================================

# # Give every employee a 10% bonus.

# df["Bonus"] = df["Salary"] * 0.10

# print("\n3. Added Bonus Column")
# print(df)

# # =====================================================
# # 4. ADD TOTAL SALARY
# # =====================================================

# # Total Salary = Salary + Bonus

# df["Total Salary"] = df["Salary"] + df["Bonus"]

# print("\n4. Added Total Salary")
# print(df)

# # =====================================================
# # 5. ADD TAX COLUMN
# # =====================================================

# # Tax = 5% of Salary

# df["Tax"] = df["Salary"] * 0.05

# print("\n5. Added Tax")
# print(df)

# # =====================================================
# # 6. ADD NET SALARY
# # =====================================================

# # Net Salary = Salary + Bonus - Tax

# df["Net Salary"] = df["Salary"] + df["Bonus"] - df["Tax"]

# print("\n6. Added Net Salary")
# print(df)

# # =====================================================
# # 7. ADD BOOLEAN COLUMN
# # =====================================================

# # Check if employee earns more than 45000.

# df["High Salary"] = df["Salary"] > 45000

# print("\n7. High Salary")
# print(df)

# # =====================================================
# # 8. ADD PERFORMANCE STATUS
# # =====================================================

# # If score is greater than 90 then Outstanding.

# df["Outstanding"] = df["Performance Score"] >= 90

# print("\n8. Outstanding Employees")
# print(df)

# # =====================================================
# # 9. ADD COLUMN USING CONDITIONAL EXPRESSION
# # =====================================================

# # Pass if score >= 80

# df["Result"] = df["Performance Score"] >= 80

# print("\n9. Result Column")
# print(df)

# # =====================================================
# # 10. ADD SERIAL NUMBER
# # =====================================================

# # Add employee ID

# df["Employee ID"] = range(101, 109)

# print("\n10. Employee ID")
# print(df)

# # =====================================================
# # 11. INSERT COLUMN AT SPECIFIC POSITION
# # =====================================================

# # Insert Gender after Employee column.

# gender = [
#     "Male",
#     "Male",
#     "Male",
#     "Female",
#     "Female",
#     "Male",
#     "Female",
#     "Male"
# ]

# df.insert(1, "Gender", gender)

# print("\n11. Insert Gender Column")
# print(df)

# # =====================================================
# # 12. COPY A COLUMN
# # =====================================================

# # Copy Salary into another column.

# df["Basic Salary"] = df["Salary"]

# print("\n12. Copy Salary")
# print(df)

# # =====================================================
# # FINAL DATAFRAME
# # =====================================================

# print("\nFinal DataFrame")
# print(df)