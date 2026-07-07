# '''
# 1- how to select any specific row
# 2- filter rows baed on conditions
# 3- combine multiple conditions 


# '''

# import pandas as pd

# # -------------------------------
# # Create Employee Dataset
# # -------------------------------

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
# # 1. SELECTING ROWS USING loc[]
# # =====================================================

# print("\n========== Select Single Row using loc ==========")
# print(df.loc[3])

# print("\n========== Select Multiple Rows using loc ==========")
# print(df.loc[[1, 3, 6]])

# print("\n========== Select Range of Rows using loc ==========")
# print(df.loc[2:5])

# # =====================================================
# # 2. SELECTING ROWS USING iloc[]
# # =====================================================

# print("\n========== Select Single Row using iloc ==========")
# print(df.iloc[3])

# print("\n========== Select Multiple Rows using iloc ==========")
# print(df.iloc[[0, 2, 5]])

# print("\n========== Select Range of Rows using iloc ==========")
# print(df.iloc[2:5])

# # =====================================================
# # 3. FILTERING ROWS
# # =====================================================

# print("\n========== Salary > 45000 ==========")
# print(df[df["Salary"] > 45000])

# print("\n========== Salary < 40000 ==========")
# print(df[df["Salary"] < 40000])

# print("\n========== Age > 25 ==========")
# print(df[df["Age"] > 25])

# print("\n========== Age < 25 ==========")
# print(df[df["Age"] < 25])

# print("\n========== Performance Score > 90 ==========")
# print(df[df["Performance Score"] > 90])

# print("\n========== Performance Score >= 90 ==========")
# print(df[df["Performance Score"] >= 90])

# print("\n========== Salary >= 50000 ==========")
# print(df[df["Salary"] >= 50000])

# print("\n========== Salary <= 40000 ==========")
# print(df[df["Salary"] <= 40000])

# print("\n========== Employee == 'Rahul' ==========")
# print(df[df["Employee"] == "Rahul"])

# print("\n========== Employee != 'Rahul' ==========")
# print(df[df["Employee"] != "Rahul"])

# # =====================================================
# # 4. MULTIPLE CONDITIONS (AND)
# # =====================================================

# print("\n========== Salary > 40000 AND Age > 25 ==========")
# print(df[(df["Salary"] > 40000) & (df["Age"] > 25)])

# print("\n========== Salary > 45000 AND Performance Score > 85 ==========")
# print(df[(df["Salary"] > 45000) & (df["Performance Score"] > 85)])

# print("\n========== Age > 24 AND Salary > 40000 AND Performance Score > 85 ==========")
# print(df[
#     (df["Age"] > 24) &
#     (df["Salary"] > 40000) &
#     (df["Performance Score"] > 85)
# ])

# # =====================================================
# # 5. MULTIPLE CONDITIONS (OR)
# # =====================================================

# print("\n========== Age < 24 OR Performance Score > 90 ==========")
# print(df[(df["Age"] < 24) | (df["Performance Score"] > 90)])

# print("\n========== Salary > 50000 OR Age < 24 ==========")
# print(df[(df["Salary"] > 50000) | (df["Age"] < 24)])

# # =====================================================
# # 6. NOT CONDITION
# # =====================================================

# print("\n========== NOT (Salary > 50000) ==========")
# print(df[~(df["Salary"] > 50000)])

# print("\n========== NOT (Performance Score >= 90) ==========")
# print(df[~(df["Performance Score"] >= 90)])

# # =====================================================
# # 7. FILTER + SELECT SPECIFIC COLUMNS
# # =====================================================

# print("\n========== Employee & Salary where Salary > 45000 ==========")
# print(df.loc[df["Salary"] > 45000, ["Employee", "Salary"]])

# print("\n========== Employee & Performance Score where Age > 25 ==========")
# print(df.loc[df["Age"] > 25, ["Employee", "Performance Score"]])

# print("\n========== Employee, Age & Salary where Performance Score >= 90 ==========")
# print(df.loc[df["Performance Score"] >= 90,
#              ["Employee", "Age", "Salary"]])

# # =====================================================
# # 8. FILTER USING isin()
# # =====================================================

# print("\n========== Employees Rahul, Priya and Sneha ==========")
# print(df[df["Employee"].isin(["Rahul", "Priya", "Sneha"])])

# # =====================================================
# # 9. FILTER USING between()
# # =====================================================

# print("\n========== Salary Between 40000 and 55000 ==========")
# print(df[df["Salary"].between(40000, 55000)])

# print("\n========== Age Between 24 and 28 ==========")
# print(df[df["Age"].between(24, 28)])

# # =====================================================
# # 10. PRACTICE QUESTIONS (TRY YOURSELF)
# # =====================================================

# # 1. Show only Rohit's record.
# # 2. Show employees whose salary is greater than 45000.
# # 3. Show employees whose age is less than 26.
# # 4. Show employees whose performance score is at least 90.
# # 5. Show employees whose salary is greater than 40000 AND age is greater than 25.
# # 6. Show employees whose age is less than 24 OR salary is greater than 50000.
# # 7. Show Employee and Salary columns for employees with performance score greater than 85.
# # 8. Show employees whose names are Mohit, Neha and Sneha.
# # 9. Show employees whose salary is between 40000 and 55000.
# # 10. Show employees except Rahul.


###############################################