import pandas as pd
import statsmodels.api as sm

source = 'https://raw.githubusercontent.com/cbrownley/foundations-for-analytics-with-python/master/statistics/winequality-both.csv'
df = pd.read_csv(source)
# print(df)
test = df.tail(10)
testy = test['quality']
testX = sm.add_constant(test[test.columns.difference(['type','quality'])])

train = df.iloc[0:-10,:]
y = train['quality']
X = sm.add_constant(train[train.columns.difference(['type','quality'])])

model = sm.OLS(y, X).fit()  #A: 建立線性回歸模型

print(model.summary())      #B: 輸出回歸結果
print(model.predict(testX)) #C: 輸入測試資料預測值
