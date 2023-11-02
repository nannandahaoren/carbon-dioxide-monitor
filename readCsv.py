import pandas as pd

file_path = "./data.csv"

data = pd.read_csv(file_path)
print(data.head())
print(data.index)
