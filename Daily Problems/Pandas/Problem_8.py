'''
Question: Rename a Column

Prompt:
Rename the column Dept to Department.

Example Input:

Name	Dept

Expected Output:
Column name changed to Department.
'''

import pandas as pd

df = pd.DataFrame(
    {
        'Name': ['A', 'B', 'C', 'D'],
        'Salary': [30000, 40000, 50000, 60000],
        'Dept': ['IT', 'HR', 'HR', 'IT']
    }
)

df.rename(columns={'Dept': 'Department'}, inplace=True)
print(df)