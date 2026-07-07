'''interpolate() is one of the smartest ways to handle missing values. Instead of replacing missing values with a fixed number (like 0, mean, or median), it estimates the missing value based on the surrounding data.'''

"""It's especially useful for:

📈 Time series data (stock prices, temperatures, sales)
📊 Continuous numerical data
📉 Sensor readings

It is not recommended for text/categorical columns like names or departments."""



########################################
########################################
########################################
########################################
#linear, polynomial, time 
import pandas as pd

data = {
    "Day": [1, 2, 3, 4, 5, 6, 7],
    "Temperature": [28, 30, None, None, 36, 38, 40]
}

df = pd.DataFrame(data)

print("Original DataFrame")
print(df)

print("\nAfter Interpolation")
print(df.interpolate())