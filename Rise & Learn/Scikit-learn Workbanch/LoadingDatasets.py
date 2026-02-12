import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris


data = load_iris()
x = data.data
y = data.target

'''
Common datasets:
    • load_iris()
    • load_digits()
    • load_wine()
    • load_breast_cancer()
'''

# From CSV
df = pd.read_csv("Enter your file name here with file formate")
X = df.drop("target", axis=1)
y = df["target"]