'''
Question: Check for Missing Values

Prompt:
Identify columns that contain missing (NaN) values.

Example Input:

Name	Age	City
A	25	NaN
B	NaN	Delhi

Expected Output:
Boolean result showing missing values per column.
'''

import pandas as pd

df = pd.DataFrame(
    {
        'Name': ['A', 'B'],
        'Age': [25, 'NaN'],
        'City': ['NaN', 'Delhi']
    }
)