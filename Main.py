import pandas as pd

# print("Pandas version:", pd.__version__)


# import pandas as pd

# students = {
#     "Name": ["Mohit", "Rahul", "Aman"],
#     "Age": [20, 21, 19],
#     "Marks": [90, 85, 95]
# }

# df = pd.DataFrame(students)

# print(df)

###########################################
#read data from CSV file into a dataframe

import pandas as pd

# df = pd.read_csv("Sales_data_sample.xlsx", sep="\t")

# print(df)
# print(df.head())

#Check the dataset shape
# print(df.shape)

#See column names
# print(df.columns)

#Get dataset information
# print(df.info())

#View summary statistics
# print(df.describe())


#Read json file 

df = pd.read_json("sample_data.json")
print(df)
