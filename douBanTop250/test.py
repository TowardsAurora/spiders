import pandas as pd

data = pd.read_excel('movie.xlsx')
values = data.values
print(values[:,1])
