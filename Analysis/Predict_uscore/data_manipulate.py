import pandas as pd

data = pd.read_csv('uscore_all.csv', encoding='ansi', index_col='uid')
print(data.head())
