'''
When you load a dataset, the first step is to understand what it contains.
Pandas provides simple methods to quickly explore the structure and content of a DataFrame.
'''
import pandas as pd
df = pd.DataFrame({
    "Name": ["John", "Rahul", "Dev", "Jack", "Rey", "Neha", "Adam", "Rohan", "Ema", "Jolly"],
    "Age": [22, 43, 54, 21, 19, 30, 22, 24, 29, 31]
})

'''
df.head(n):
Returns the first n rows of the DataFrame.
    • Default value of n is 5
    • Used to quickly check how the data starts
'''
print(df.head())


'''
df.tail(n):
Returns the last n rows of the DataFrame.
    • Default value of n is 5
    • Useful to verify the end of the dataset
'''
print(df.tail())


'''
df.info():
Gives a concise summary of the DataFrame.

It shows:
    • Number of rows and columns
    • Column names
    • Data types of each column
    • Count of non-null values
    • Memory usage
'''
print(df.info())


'''
df.describe():
Generates descriptive statistics for numerical columns.

Includes:
    • Count
    • Mean
    • Standard deviation
    • Minimum value
    • 25%, 50% (median), 75%
    • Maximum value
'''
print(df.describe())

# To include categorical columns:
df.describe(include="all")


'''
df.shape:
Returns the dimensions of the DataFrame.
    • Output format: (number_of_rows, number_of_columns)
    • It is a property, not a method
'''
print(df.shape)