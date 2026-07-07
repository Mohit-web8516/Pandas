import pandas as pd

data = {
    "Name":['Ram','Shyam','Rahul'],
    "Age":[10,20,30],
    "City":['Nagpur','Delhi','Mumbai']
}

df = pd.DataFrame(data)
print('Display the info of data set')
print(df.info())



# df = pd.read_json("sample_data.json")
# print('----------------------------')
# print(df.info())