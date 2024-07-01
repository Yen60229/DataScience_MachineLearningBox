import pandas as pd


df = pd.read_csv('https://raw.githubusercontent.com/kiang/pharmacies/master/data.csv')
top5 = df.groupby('縣市').size().sort_values(ascending=False).head(5) # type: ignore
print(top5)
