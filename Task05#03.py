import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()
df = pd.DataFrame(data= np.c_[iris['data'], iris['target']], # type: ignore
                     columns= iris['feature_names'] + ['target']) # type: ignore

# 1. 利用資料視覺化觀察 sepal 和 petal 四個欄位的關係。
plt.plot(df['sepal length (cm)'], label='Sepal Length')
plt.plot(df['sepal width (cm)'], label='Sepal Width')
plt.plot(df['petal length (cm)'], label='petal Length')
plt.plot(df['petal width (cm)'], label='petal Width')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()
plt.show()

#2. 利用相關係數觀察 sepal 和 petal 四個欄位的關係。
corr_iris = df[iris['feature_names']].corr() # type: ignore
print(corr_iris)
