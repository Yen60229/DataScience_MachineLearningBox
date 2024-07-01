import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 給定的資料集
X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])

print('===== 原始資料 =====')
df = pd.DataFrame(X)
print(df)
print("  ")

# 要比較的k值
k_values = [3, 4, 5]

# 創建 subplot
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

for i, k in enumerate(k_values):

    # 建立 KMeans 分群器
    kmeans = KMeans(n_clusters=k, random_state=42)
    
    # 對訓練集進行訓練
    kmeans.fit(X)
    
    # 繪製分群結果
    axs[i].scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis')
    axs[i].scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='*', color='red', s=100)
    axs[i].set_title(f'K={k}')
    
    # 分群結果的數字相同，圖上顯示顏色相同、同一群；分群中心表示同一群的中心點
    print(f"k = {k} 分群結果：\n", kmeans.labels_)
    print(f"k = {k} 分群中心：\n", kmeans.cluster_centers_)
    print("\n")
    
# 顯示subplot   
plt.tight_layout()
plt.show()

"""
6筆資料好比6位學生在小教室來分群，分成3群的分群中心與結果較符合比例，分群中心>3 會出現至少兩組資料數少於1，分類可能因此失去意義。
"""
