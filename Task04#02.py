import numpy as np
import pandas as pd
import sqlite3



raw_data = {'first_name': ['Jason', np.nan, 'Tina', 'Jake', 'Amy'], 
        'last_name': ['Miller', np.nan, 'Ali', 'Milner', 'Cooze'], 
        'age': [42, np.nan, 36, 24, 73], 
        'sex': ['m', np.nan, 'f', 'm', 'f'], 
        'preTestScore': [4, np.nan, np.nan, 2, 3],
        'postTestScore': [25, np.nan, np.nan, 62, 70]}

df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'sex', 'preTestScore', 'postTestScore'])

# Drop missing observations
drop_na = df.dropna()
conn = sqlite3.connect('hw#04-raw_data_drop_na.db')
drop_na.to_sql('hw#04-raw_data_drop_na', conn, if_exists='replace', index=False)
conn.close()

#Drop rows where all cells in that row is NA
drop_all_missing = df.dropna(thresh = 1)
conn = sqlite3.connect('hw#04-raw_data_drop_all_missing.db')
drop_all_missing.to_sql('hw#04-raw_data_drop_all_missing', conn, if_exists='replace', index=False)
conn.close()

#Create a new column full of missing values
df['NaN'] = np.nan
conn = sqlite3.connect('hw#04-raw_data_with_nan.db')
df.to_sql('hw#04-raw_data_with_nan', conn, if_exists='replace', index=False)
conn.close()

#Fill in missing data with zeros
df.fillna(0, inplace = True)
conn = sqlite3.connect('hw#04-raw_data_fillna.db')
df.to_sql('hw#04-raw_data__fillna', conn, if_exists='replace', index=False)
conn.close()

#Fill in missing in preTestScore with the mean value of preTestScore
df.preTestScore = df.preTestScore.fillna(df.preTestScore.mean())
conn = sqlite3.connect('hw#04-raw_data_PreTestScore.db')
df.to_sql('hw#04-raw_data__PreTestScore', conn, if_exists='replace', index=False)
conn.close()

#Fill in missing in postTestScore with each sex’s mean value of postTestScore
df.postTestScore = df.groupby('sex').postTestScore.transform(lambda x : x.fillna(x.mean()))
conn = sqlite3.connect('hw#04-raw_data_postTestScore.db')
df.to_sql('hw#04-raw_data_postTestScore', conn, if_exists='replace', index=False)
conn.close()

#Select some rows but ignore the missing data points
df = df.dropna(how='any')
conn = sqlite3.connect('hw#04-raw_data_ignore_miss.db')
df.to_sql('hw#04-raw_data_ignore_miss', conn, if_exists='replace', index=False)
conn.close()

