'''
Pandas can read data stored in JSON format and convert it directly into a DataFrame.
JSON is very common when working with APIs, logs, and web data.

What is JSON?
JSON stands for JavaScript Object Notation.
It stores data as key–value pairs, very similar to a Python dictionary.

Example:
{
  "name": "Amit",
  "age": 21,
  "marks": 85
}
'''
import pandas as pd


'''
Read JSON file using Pandas
If you have a JSON file:
'''
df = pd.read_json("data.json")
print(df)


'''
Dictionary as JSON (Python Dictionary → DataFrame)
A Python dictionary can act like JSON data.
'''
# Simple dictionary
data = {
    "Name": ["Amit", "Neha", "Rahul"],
    "Age": [20, 21, 22],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)
print(df)


# Dictionary of dictionaries
data = {
    "Amit": {"Age": 20, "Marks": 85},
    "Neha": {"Age": 21, "Marks": 90}
}

df = pd.DataFrame(data)
print(df)


'''
4. Read JSON string directly
Sometimes JSON comes as a string (API response).
'''
json_data = """
[
  {"Name": "Amit", "Age": 20, "Marks": 85},
  {"Name": "Neha", "Age": 21, "Marks": 90}
]
"""

df = pd.read_json(json_data)
print(df)


'''
Common issue: Nested JSON
JSON often contains nested data. Pandas provides json_normalize to flatten it.

Example idea:
pd.json_normalize(data)


Quick summary:
    • read_json() reads JSON files or JSON strings
    • Python dictionaries are already JSON-like
    • Keys usually become columns
    • Nested JSON may need flattening
'''

