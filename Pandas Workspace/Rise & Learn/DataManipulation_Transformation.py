import pandas as pd

data = {
    "EmployeeID": [101, 102, 103, 104, 105, 106],
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Ankit", "Neha"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT"],
    "Region": ["North", "South", "North", "East", "West", "South"],
    "Salary": [50000, 45000, 55000, 60000, 48000, 52000],
    "Month": ["Jan", "Jan", "Feb", "Feb", "Jan", "Feb"]
}
df1 = pd.DataFrame(data)

dept_data = {
    "Department": ["IT", "HR", "Finance"],
    "Manager": ["Rohit", "Kavita", "Suresh"]
}
df2 = pd.DataFrame(dept_data)


'''
Once data is loaded and cleaned, the next step is to reshape, combine, and transform it.
Pandas provides powerful functions to do this efficiently.

merge() – Combine DataFrames (SQL-style joins)
Used to join two DataFrames using a common key.

Common joins:
    • inner
    • left
    • right
    • outer
'''
# Example:
pd.merge(df1, df2, on="id", how="inner")


'''
concat() – Stack or combine data
Used to concatenate Pandas objects along a given axis.
'''
# Examples:
pd.concat([df1, df2])
pd.concat([df1, df2], axis=1)


'''
groupby() – Group and aggregate data
Groups data based on one or more columns and applies aggregation.

Common aggregations:
    • sum
    • mean
    • count
    • min / max
'''
# Example:
df1.groupby("Department")["Salary"].mean()


'''
pivot_table() – Spreadsheet-style summary
Creates a pivot table similar to Excel.
'''
# Example:
pd.pivot_table(
    df1,
    values="Sales",
    index="Region",
    columns="Month",
    aggfunc="sum"
)


'''
sort_values() – Sort data
Sorts the DataFrame by column values.
'''
# Example:
df1.sort_values("Marks")
df1.sort_values("Marks", ascending=False)


'''
apply() – Apply custom functions
Applies a function across rows or columns.
'''
# Example:
df1["Bonus"] = df1["Salary"].apply(lambda x: x * 0.1)


'''
value_counts() – Count unique values
Returns frequency of unique values in a column or Series.
'''
# Example:
df1["Department"].value_counts()