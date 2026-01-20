'''
A Pandas Series is a one-dimensional data structure that can store data of any type.
You can think of it as a single column of a table,
but with one important extra feature: labels (index) for each value.

Key characteristics of a Series:
    • One-dimensional
    • Has an index (labels for data)
    • Can store integers, floats, strings, or even mixed types
    • Built on top of NumPy, so operations are fast
'''
import pandas as pd

'''
Creating a Series
From a list
'''
data = [10, 20, 30, 40]
s = pd.Series(data)
print(s)


# From a list with custom index
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])


# From a dictionary
data = {'Math': 85, 'Science': 90, 'English': 88}
s = pd.Series(data)



'''
Data Labels (Index)

Data labels in Pandas are called the Index.

What they do:
    • Identify each data value
    • Make data easy to access
    • Help align data during operations

Key points about labels:
    • They can be numbers, strings, or dates
    • They do not have to be unique (though usually they are)
    • If you don’t provide labels, Pandas creates them automatically (0, 1, 2, ...)

Example idea:

Index:  a   b   c
Data:  10  20  30

Here:
a, b, c are data labels
10, 20, 30 are data values    
'''
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)


'''
DataFrame

A DataFrame is a two-dimensional structure.
It is made up of multiple Series.

You can think of a DataFrame as:
    • A table with rows and columns
    • Each column is a Series
    • Each row is identified by an index (row labels)
'''
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)
print(myvar)


'''
Relationship between Series and DataFrame
    • A Series = single column with labels
    • A DataFrame = collection of Series sharing the same index

Simple way to remember:
    • Series → 1D labeled data
    • DataFrame → 2D labeled data (table)
'''