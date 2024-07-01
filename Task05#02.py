import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.random(100)*100)
n = int(input())

df['binned'] = pd.qcut(df[0], q = n, labels=False)
print(df)
