'''
Question: Group By Column

Prompt:
Calculate the average salary for each department.

Example Input:

Dept	Salary
IT	40000
HR	30000
IT	50000

Expected Output:
Average salary per department.
'''

import pandas as pd

df = pd.DataFrame(
    {
        'Dept': ['IT', 'HR', 'IT', 'HR', 'IT'],
        'Salary': [40000, 30000, 50000, 45000, 55000]
    }
)

