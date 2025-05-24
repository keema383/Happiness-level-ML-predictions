import pandas as pd

df = pd.read_stata('data.dta')

# Check the first few rows of the dataset
print(df.head())
print(df.columns)

df.to_csv('data.csv', index=False)
