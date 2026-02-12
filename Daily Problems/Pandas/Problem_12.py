'''
Question: Sort DataFrame

Prompt:
Sort the DataFrame by Salary in descending order.

Example Input:

Name	Salary
A	30000
B	45000

Expected Output:
Rows sorted from highest to lowest salary.
'''

import pandas as pd

df = pd.DataFrame(
    {
        'Name': ['A', 'B'],
        'Salary': [45000, 30000]
    }
)

sort_salary = df.sort_values(by='Salary')
print(sort_salary)