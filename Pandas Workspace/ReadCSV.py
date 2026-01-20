'''
read_csv is used to load data from a CSV file into a Pandas DataFrame.
This is usually the first step in any data analysis task.

Basic idea:
    • CSV file → Pandas DataFrame
    • Rows become records
    • Columns become fields
'''
import pandas as pd

# Read a CSV file
df = pd.read_csv("Enter your file name here")
print(df)


'''
What is max_rows?

max_rows controls how many rows Pandas displays, not how many rows it reads.

Important point:
    • The CSV file is fully loaded
    • Only the display is limited
This is useful when working with large datasets.

Default behavior

By default, Pandas shows 60 rows:
    • First 30 rows
    • Last 30 rows
    • Middle rows are hidden
'''

# Check current max_rows
print(pd.options.display.max_rows)


# Set max_rows
pd.options.display.max_rows = 100


# how all rows
pd.options.display.max_rows = None


'''
Limit rows while reading (different from max_rows)
If you want to read only a few rows from the file, use nrows:
'''
df = pd.read_csv("data.csv", nrows=10)
print(df)


'''
Difference to remember:
    • max_rows → controls display
    • nrows → controls how much data is read

Quick summary:
    • read_csv() loads CSV files into DataFrames
    • max_rows limits visible rows, not loaded rows
    • Use nrows for performance with large files
'''