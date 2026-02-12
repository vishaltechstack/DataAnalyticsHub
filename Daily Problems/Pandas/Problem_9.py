'''
Question: Remove a Column

Prompt:
Delete the Age column from the DataFrame.

Example Input:

Name	Age	City

Expected Output:
DataFrame without the Age column.
'''

import pandas as pd

df = pd.DataFrame(
    {
        'Name': ['Rahul', 'Ankit', 'Neha'],
        'Age': [23, 25, 22],
        'City': ['Delhi', 'Mumbai', 'Pune']
    }
)
df.drop(['Age'], axis=1, inplace=True)
print(df)