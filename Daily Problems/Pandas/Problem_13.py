'''
Question: Count Unique Values

Prompt:
Find the number of unique departments.

Example Input:

Dept
IT
HR
IT

Expected Output:
A single integer showing unique count.
'''

import pandas as pd

df = pd.DataFrame(
    {
        'Dept': ['IT', 'HR', 'IT']
    }
)

unique_value = df['Dept'].unique()
print(unique_value)