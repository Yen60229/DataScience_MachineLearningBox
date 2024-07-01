import pandas as pd
import numpy as np

d = [
    {'city': 'Austin', 'visitor': 139, 'weekday': 'Sun'},
    {'city': 'Dallas', 'visitor': 237, 'weekday': 'Sun'},
    {'city': 'Austin', 'visitor': 326, 'weekday': 'Mon'},
    {'city': 'Dallas', 'visitor': 456, 'weekday': 'Mon'}
]

df = pd.DataFrame(d)

grouped = df.groupby('weekday')
result = grouped.agg({'visitor': 'sum'})
print(result)
