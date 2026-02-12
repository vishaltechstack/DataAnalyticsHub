import polars as pl

# Excel File
df = pl.read_csv("Dataset.xlsx")
print(df.head())
