import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

data['is_robot'] = 0
data['is_human'] = 0

for index, row in data.iterrows():
    if row['whoAmI'] == 'robot':
        data.at[index, 'is_robot'] = 1
    else:
        data.at[index, 'is_human'] = 1

data = data.drop(columns=['whoAmI'])

print(data.head())
