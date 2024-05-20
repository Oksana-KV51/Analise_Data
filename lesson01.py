import  pandas as pd

df = pd.read_csv('Global Ecological Footprint 2023.csv', encoding='latin1')
print(df.head(5))
print(df.describe())
print(df.info())

df_1 = pd.read_csv('dz.csv')
print(df_1.head())
print(df_1.describe())
print(df_1.info())
average_salary_by_city = df_1.groupby('City')['Salary'].mean()
# Выводим результат
print(f'средняя зарплата по городам\n {average_salary_by_city}')








