import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

"""
1
"""
# 載入波士頓房價資料集
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None) # type: ignore
features = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]

from sklearn.model_selection import train_test_split

# 切割資料集為訓練集和測試集
train_features, test_features, train_target, test_target = train_test_split(features, target, test_size=0.2)


"""
2   訓練模型之前，我們需要對資料進行預處理。這可能包括特徵縮放、類別特徵編碼、缺失值處理等。您可以使用 Python 的資料處理庫（如 scikit-learn）來執行這些預處理步驟。
"""

"""
3  使用 PyTorch，我們可以使用它的 torch.nn 模組來構建模型。以下是一個簡單的MLP範例：
"""
# 定義自定義模型
class HousePricePredictor(nn.Module):
    def __init__(self, input_size):
        super(HousePricePredictor, self).__init__()
        self.fc1 = nn.Linear(input_size, 64)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 1)
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        return x
        
"""
4 使用 PyTorch 的優化器和損失函數來訓練模型
"""
# 定義設備
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 創建模型實例
model = HousePricePredictor(input_size=13).to(device)

# 定義損失函數和優化器
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 設定訓練迴圈
num_epochs = 100
for epoch in range(num_epochs):
    # 將特徵和目標轉換為 Tensor
    features_tensor = torch.Tensor(features).to(device)
    target_tensor = torch.Tensor(target).unsqueeze(1).to(device)
    
    # 正向傳播
    outputs = model(features_tensor)
    loss = criterion(outputs, target_tensor)
    
    # 反向傳播和參數更新
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    # 每隔 10 個迭代顯示一次損失
    if (epoch + 1) % 10 == 0:
        print(f"Epoch {epoch+1}/{num_epochs}, Loss: {loss.item():.4f}")
        
"""
5  使用測試集來評估模型的性能
"""
# 將特徵轉換為 Tensor
test_features_tensor = torch.Tensor(test_features).to(device)

# 預測房價
with torch.no_grad():
    model.eval()
    predictions = model(test_features_tensor)

# 轉換為 NumPy 陣列
predictions = predictions.cpu().numpy()

# 計算評估指標（例如均方根誤差）
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(test_target, predictions)
rmse = np.sqrt(mse)
print(f"Root Mean Squared Error: {rmse:.4f}")
