'''
Question: Display First & Last 5 Rows

Prompt:
Create a DataFrame and display the first and last 5 records.

Example Input:
A DataFrame containing 12 rows of data.

Expected Output:
First and last 5 rows of the DataFrame.
'''

import pandas as pd

df = pd.DataFrame(
    {
        'Name': ['Rahul', 'Ankit', 'Sohan', 'Mohan', 'Rohit', 'Anjali', 'Khushi', 'Vini', 'Chandu', 'Kana', 'Gulshan', 'Priya'],
        'Age': [23, 21, 20, 26, 22, 25, 27, 28, 19, 21, 26, 29]
    }
)

print(df.head())
print(df.tail())