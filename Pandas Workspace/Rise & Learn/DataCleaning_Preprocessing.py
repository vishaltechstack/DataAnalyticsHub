'''
Before analysis, data usually needs cleaning.
Pandas provides simple and powerful functions to handle missing values, duplicates, and data type issues.
'''
import pandas as pd
df = pd.DataFrame({
    "Name": ["John", "Rahul", "Dev", "Jack", "Rey", "Neha", "Adam", "", "Rohan", "Ema", "Jolly"],
    "Age": [22, 43, 54, 21, 35, 19, 30, 22, 24, 29, 31]
})

'''
Detecting Missing Values:

df.isnull() or df.isna()
Checks missing values and returns a DataFrame of True / False.
    • True → value is missing (NaN)
    • False → value is present
'''
print(df.isnull())


'''
df.notna() or df.notnull()
Opposite of isnull().
    • True → value is not missing
    • False → value is missing
'''
print(df.notna())


'''
Removing Missing Values

df.dropna()
Removes rows (or columns) that contain missing values.

Default behavior:
Drops rows with at least one missing value
'''
df.dropna()

# Drop columns instead:
df.dropna(axis=1)


'''
Filling Missing Values:

df.fillna(value)
Replaces missing values with a specified value.
'''
df.fillna(0)

# Fill using column-specific values:
df.fillna({"Age": 0, "Marks": df["Marks"].mean()})


'''
Handling Duplicate Data:

df.drop_duplicates()
Removes duplicate rows from the DataFrame.
'''
df.drop_duplicates()

# Remove duplicates based on specific columns:
df.drop_duplicates(subset=["Name"])


'''
Date and Time Conversion:

pd.to_datetime()
Converts strings or numbers into datetime objects.
'''
df["Date"] = pd.to_datetime(df["Date"])


'''
Data Type Conversion:

df['col'].astype(new_type)
Changes the data type of a column.
'''
df["Age"] = df["Age"].astype(int)
df["Marks"] = df["Marks"].astype(float)