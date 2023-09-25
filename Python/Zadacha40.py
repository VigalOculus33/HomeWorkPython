import pandas as pd

data = pd.read_csv('sample_data/california_housing_train.csv')

filtered_data = data[(data['population'] > 0) & (data['population'] <= 500)]

average_house_value = filtered_data['median_house_value'].mean()

print(f"Средняя стоимость дома, где население от 0 до 500: ${average_house_value:.2f}")
