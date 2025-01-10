import pandas as pd

df = pd.read_csv('diamonds.csv')

print(df.head())

print(df.info())

print(df.describe())

df = pd.read_csv('dz.csv')

print(df)

group = df.groupby('City')['Salary'].mean()

print(group)
