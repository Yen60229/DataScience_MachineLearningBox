import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split

source = 'https://raw.githubusercontent.com/MachineLearningLiuMing/scikit-learn-primer-guide/master/Data.csv'

df = pd.read_csv(source)

"""
分類學習
"""

# country用one-hot-encoding轉換
dummy_df = pd.get_dummies(df["Country"], dtype=int)
#填補缺失值
df.fillna({"Age" : df["Age"].median()}, inplace= True)
df.fillna({"Salary" :df["Salary"].median()}, inplace= True)
#切片選取
x= pd.concat([df[["Age" ,"Salary"]], dummy_df], axis = 1)
y = df["Purchased"]

# 切分訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# 創建分類樹模型
from sklearn.tree import DecisionTreeClassifier
clf_model = DecisionTreeClassifier()

# 訓練模型
clf_model.fit(X_train, y_train)

# 使用模型進行預測
y_pred_clf = clf_model.predict(X_test)

# 將 y_pred_clf 轉換成 DataFrame
y_pred_clf_df = pd.DataFrame(y_pred_clf, columns=['Prediction'])

# 使用tail()印出最後三個預測值
print("利用 Country, Age, Salary 對 Purchased 進行分類學習，印出後三筆資料的 Purchased 為", y_pred_clf_df.tail(3))


"""
回歸學習
"""

# country用one-hot-encoding轉換
dummy_df = pd.get_dummies(df["Country"], dtype=int)

#填補缺失值
df.fillna({"Age" : df["Age"].median()}, inplace= True)
df.fillna({"Salary" :df["Salary"].median()}, inplace= True)
#將yes,no轉換
label_encoder = LabelEncoder()
df['Purchased'] = label_encoder.fit_transform(df['Purchased'])
#切片選取
x= pd.concat([df[["Age" ,"Purchased"]], dummy_df], axis = 1)
y = df["Salary"]
# 切分訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# 創建回歸樹模型
from sklearn.tree import DecisionTreeRegressor
reg_model = DecisionTreeRegressor()

# 訓練模型
reg_model.fit(X_train, y_train)

# 使用模型進行預測
y_pred_reg = reg_model.predict(X_test)

# 將 y_pred_reg 轉換成 DataFrame
y_pred_reg_df = pd.DataFrame(y_pred_reg, columns=['Prediction'])

# 使用tail()印出最後三個預測值
print("利用 Country, Age, Purchased 對 Salary 進行回歸學習，印出後三筆資料的Salary為", y_pred_reg_df.tail(3))
