import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm



#案例分析：隨機挑選了30位患者，將其隨機分成三組，每組10人，
# 分別給予不同藥物的治療。治療結束後，我們記錄每位患者的治療效果，即治療後的疾病症狀程度。

# 創建數據
data = {'group': ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
                  'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B',
                  'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C'],
        'effect': [3.1, 3.3, 3.2, 2.8, 2.9, 3.5, 3.4, 2.9, 3.2, 3.0,
                   2.8, 2.7, 2.5, 2.4, 2.9, 2.6, 2.5, 2.7, 2.8, 2.6,
                   1.9, 2.1, 1.8, 1.7, 2.0, 2.2, 2.1, 1.9, 1.8, 1.7]}

df = pd.DataFrame(data)

model =ols('effect ~ group', data = df).fit()

# 進行ANOVA分析
anova_results = anova_lm(model)

# 輸出結果
print(anova_results)
