'''
Question: Select Multiple Columns

Prompt:
Extract and display the Name and Dept columns.

Example Input:
Name	Salary	Dept

Expected Output:
A DataFrame containing only Name and Dept.
'''

import pandas as pd

df = pd.DataFrame(
    {
        'Name': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
        'Salary': [30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],
        'Dept': ['IT', 'HR', 'HR', 'IT', 'HR', 'IT', 'HR', 'IT']
    }
)

mul_value = df[['Name', 'Dept']]
print(mul_value)