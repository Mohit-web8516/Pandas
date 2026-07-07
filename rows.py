'''1. head() → View the first rows
Why?

Datasets can contain thousands or millions of rows. Printing everything is inefficient.

Instead:

print(df.head())

Want the first 10?

print(df.head(10))'''

import pandas as pd

df = pd.read_json("sample_data.json")

print('Display 10 rows of first')
print(df.head())

print('Display 10 rows of last')
print(df.tail())


