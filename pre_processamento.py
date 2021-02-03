import pandas as pd

base = pd.read_csv('credit_data.csv', encoding='latin1')
base.describe()
print(base.head())
