import pandas as pd

data = {
    "Name":['Ram','Shyam','Rahul'],
    "Age":[10,20,30],
    "City":['Nagpur','Delhi','Mumbai']
}

df = pd.DataFrame(data)
print(df)

#####################################
## How to save a data


#to save as a  csv file
# df.to_csv("output.csv",index = False)

#to save as a excel file
df.to_excel("output.xlsx",index = False)

#to save as a json file
df.to_json("output.json",index = False)

