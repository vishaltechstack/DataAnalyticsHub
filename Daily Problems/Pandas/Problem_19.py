'''
Question: Replace Values

Example input:

Name            Gender
A               Male
B               Female

Expected Output:
Gender values replaced.
'''
import pandas as pd

data = {
    "Name": ["A", "B"],
    "Gender": ["Male", "Female"]
}

df = pd.DataFrame(data)
print(df.replace[""])