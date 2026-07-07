# import pandas as pd

# # Employee Information
# employee = {
#     "Employee ID": [101, 102, 103, 104],
#     "Name": ["Mohit", "Rahul", "Aman", "Priya"],
#     "Department": ["IT", "HR", "Finance", "Marketing"]
# }

# df_employee = pd.DataFrame(employee)

# # Salary Information
# salary = {
#     "Employee ID": [101, 102, 103, 105],
#     "Salary": [35000, 42000, 50000, 60000]
# }

# df_salary = pd.DataFrame(salary)

# print("Employee Data")
# print(df_employee)

# print("\nSalary Data")
# print(df_salary)

################################
################################
################################
################################


import pandas as pd

employee = {
    "Employee ID":[101,102,103,104],
    "Name":["Mohit","Rahul","Aman","Priya"],
    "Department":["IT","HR","Finance","Marketing"]
}

salary = {
    "Employee ID":[101,102,103,105],
    "Salary":[35000,42000,50000,60000]
}

df_employee = pd.DataFrame(employee)
df_salary = pd.DataFrame(salary)

print("Employee Data")
print(df_employee)

print("\nSalary Data")
print(df_salary)

print("\nInner Merge")
print(pd.merge(df_employee, df_salary, on="Employee ID", how="inner"))

print("\nLeft Merge")
print(pd.merge(df_employee, df_salary, on="Employee ID", how="left"))

print("\nRight Merge")
print(pd.merge(df_employee, df_salary, on="Employee ID", how="right"))

print("\nOuter Merge")
print(pd.merge(df_employee, df_salary, on="Employee ID", how="outer"))