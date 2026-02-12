'''
Question: Select a Single Column

Prompt:
Display only the Salary column from the given DataFrame.

Example Input:

Name	Salary	Dept
A	30000	IT
B	40000	HR

Expected Output:
A single column showing salary values.
'''

import pandas as pd

df = pd.DataFrame(
    {
        'Name': ['A', 'B', 'C', 'D'],
        'Salary': [30000, 40000, 50000, 60000],
        'Dept': ['IT', 'HR', 'HR', 'IT']
    }
)

sal_value = df['Salary']
print(sal_value)