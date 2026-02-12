'''
Question: Create a DataFrame

Prompt:
Create a Pandas DataFrame from the given data and display it.

Example Input:

Name: Rahul, Ankit, Neha
Age: 23, 25, 22
City: Delhi, Mumbai, Pune


Expected Output:

   Name   Age     City
0  Rahul  23   Delhi
1  Ankit  25   Mumbai
2  Neha   22   Pune
'''

import pandas as pd

dff = pd.DataFrame({'Name': ['Rahul', 'Ankit', 'Neha'], 'Age': [23, 25, 22], 'City': ['Delhi', 'Mumbai', 'Pune']})
print(dff)