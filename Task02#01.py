import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
print(df)
# - 1. filtered by first column > 20?
mask1 = df[0] > 20
print(df[mask1])
# - 2. filtered by first column + second column > 50
mask2 = df[0] + df[1] > 50
print(df[mask2])

# - 3. filtered by first column < 30 or second column > 30
mask3 = (df[0] < 30) | (df[1] > 30)
print(df[mask3])

# - 4. filtered by total sum of row > 100
mask4 = df.sum(axis = 1) > 100
print(df[mask4])
