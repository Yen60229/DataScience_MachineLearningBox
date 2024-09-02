import pandas as pd
import numpy as np
import sqlite3

url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'
df = pd.read_csv(url)
#Count the number of missing values in each column and find the maximum number of missing values.
print(df.isnull().sum().max())

# How to replace missing values of 'multiple numeric' columns with the mean?
cols_mean = df.select_dtypes(include=[np.number]).mean()
df.fillna(cols_mean, inplace=True)
conn = sqlite3.connect('Cars93-miss.db')
df.to_sql('Cars93-miss', conn, if_exists='replace', index=False)
conn.close()

# Calculate the average price of different manufacturers.
mean_price = df.groupby("Manufacturer")["Price"].mean()
print(mean_price)

#How to replace missing values of `price` columns with the mean depending on its manufacturers?
df10 = df * 1
price_na = df10['Price'].isna()
for i in df10.index:
    if price_na.loc[i]:
        df10.loc[i, 'Price'] = mean_price[df10.loc[i, 'Manufacturer']]   
           
conn = sqlite3.connect('Cars93-miss.db')
df.to_sql('Cars93-miss', conn, if_exists='replace', index=False)
conn.close()
