'''
Question: Check DataFrame Shape

Prompt:
Find the number of rows and columns in the given DataFrame.

Example Input:
A DataFrame with student records.

Expected Output:

(rows, columns)
'''

import pandas as pd

df = pd.DataFrame(
    {
        'Name': ['Rahul', 'Ankit', 'Sohan', 'Mohan', 'Rohit', 'Anjali', 'Khushi', 'Vini', 'Chandu', 'Kana', 'Gulshan', 'Priya'],
        'Age': [23, 21, 20, 26, 22, 25, 27, 28, 19, 21, 26, 29]
    }
)

print(df.shape)