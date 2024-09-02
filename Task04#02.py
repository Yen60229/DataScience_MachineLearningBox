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
df1 = df * 1
drop_na = df1.dropna()
conn = sqlite3.connect('hw#04-raw_data_drop_na.db')
drop_na.to_sql('hw#04-raw_data_drop_na', conn, if_exists='replace', index=False)
conn.close()

#Drop rows where all cells in that row is NA
df2 = df * 1
drop_all_missing = df2.dropna(thresh = 1)
conn = sqlite3.connect('hw#04-raw_data_drop_all_missing.db')
drop_all_missing.to_sql('hw#04-raw_data_drop_all_missing', conn, if_exists='replace', index=False)
conn.close()

#Create a new column full of missing values
df3 = df * 1
df3['NaN'] = np.nan
conn = sqlite3.connect('hw#04-raw_data_with_nan.db')
df3.to_sql('hw#04-raw_data_with_nan', conn, if_exists='replace', index=False)
conn.close()

#Fill in missing data with zeros
df4 = df3.fillna(0)
conn = sqlite3.connect('hw#04-raw_data_fillna.db')
df4.to_sql('hw#04-raw_data__fillna', conn, if_exists='replace', index=False)
conn.close()

#Fill in missing in preTestScore with the mean value of preTestScore
df5 = df4 * 1
#布爾序列來篩選和過濾raw_data的NULL值
filtered_df = df[df['preTestScore'].notna()]
preTestScore_mean = filtered_df['preTestScore'].mean()
preTestScore_na = df['preTestScore'].isna()

for i in df['preTestScore'].index:
        if preTestScore_na.loc[i]:
             df5.loc[i, 'preTestScore'] =  preTestScore_mean
             
conn = sqlite3.connect('hw#04-raw_data_PreTestScore.db')
df5.to_sql('hw#04-raw_data__PreTestScore', conn, if_exists='replace', index=False)
conn.close()

#Fill in missing in postTestScore with each sex’s mean value of postTestScore
df6 = df5 * 1

# 過濾掉 preTestScore 為 NaN 的行，只保留 sex 和 postTestScore 列
filtered_df = df[df['preTestScore'].notna()][['sex', 'postTestScore']]

grouped_scores = filtered_df.groupby('sex')['postTestScore'].sum()
print(grouped_scores)  
                   
preTestScore_na = df['postTestScore'].isna()
for i in df['postTestScore'].index:
    if preTestScore_na.loc[i]:
        if df.loc[i, 'sex'] == 'f':
            df6.loc[i, 'postTestScore'] = grouped_scores['f']    
        if df.loc[i, 'sex'] == 'm':
            df6.loc[i, 'postTestScore'] = grouped_scores['m'] 
  
conn = sqlite3.connect('hw#04-raw_data_postTestScore.db')
df6.to_sql('hw#04-raw_data_postTestScore', conn, if_exists='replace', index=False)
conn.close()

#Select some rows but ignore the missing data points
df = df.dropna(how='any')
conn = sqlite3.connect('hw#04-raw_data_ignore_miss.db')
df.to_sql('hw#04-raw_data_ignore_miss', conn, if_exists='replace', index=False)
conn.close()
