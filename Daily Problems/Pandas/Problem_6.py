'''
Question: Filter Rows Based on Condition

Prompt:
Display employees whose salary is greater than 35,000.

Example Input:

Name	Salary
A	30000
B	45000
C	38000

Expected Output:
Rows where salary is greater than 35,000.
'''

import pandas as pd

df = pd.DataFrame(
    {
        'Name': ['A', 'B', 'C'],
        'Salary': [30000, 45000, 38000]
    }
)

find_salary = df.loc[df['Salary'] > 35000]
print(find_salary)