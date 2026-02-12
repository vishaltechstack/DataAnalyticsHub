'''
Question: Count Rows

Prompt:
Find the total number of rows in the DataFrame.

Example Input:
A DataFrame with student records.

Expected Output:
A single integer showing rows count.
'''
import pandas as pd

data = {
    "Name": ["John", "Jane", "Martin", "Nikki", "Miz"],
    "Age": [23, 20, 21, 25, 19],
    "Marks": [88, 70, 69, 90, 75]
}
S_data = pd.DataFrame(data)
rows, column = S_data.shape
print(f"Number of rows: {rows}")
print(f"Number of columns: {column}")