'''
Question: Add a New Column

Prompt:
Add a new column Bonus with a fixed value of 5000 for all employees.

Example Input:
Name	Salary

Expected Output:
A new column Bonus added to the DataFrame.
'''

import pandas as pd

df = pd.DataFrame(
    {
        'Name': ['A', 'B', 'C', 'D'],
        'Salary': [30000, 40000, 50000, 60000],
        'Dept': ['IT', 'HR', 'HR', 'IT']
    }
)

# First example:
df['Bonus'] = [5000, 5000, 5000, 5000]
print(df)

# Second example:
df.insert(loc=3, column='Bonus', value=[5000, 5000, 5000, 5000])
print(df)