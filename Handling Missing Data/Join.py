import pandas as pd

employee = pd.DataFrame(
    {
        "Employee": ["Mohit", "Rahul", "Aman", "Priya"],
        "Department": ["IT", "HR", "Finance", "Marketing"]
    },
    index=[101, 102, 103, 104]
)

salary = pd.DataFrame(
    {
        "Salary": [35000, 42000, 50000, 70000]
    },
    index=[101, 102, 103, 105]
)

print("Employee Data")
print(employee)

print("\nSalary Data")
print(salary)

print("\nLeft Join")
print(employee.join(salary, how="left"))

print("\nRight Join")
print(employee.join(salary, how="right"))

print("\nInner Join")
print(employee.join(salary, how="inner"))

print("\nOuter Join")
print(employee.join(salary, how="outer"))