import pandas as pd
import matplotlib.pyplot as plt

# Чтение исходного CSV файла
input_file = 'sofas_prices.csv'
df = pd.read_csv(input_file)

# Извлечение столбца 'Цена' и преобразование в целые числа
df['Цена'] = df['Цена'].apply(lambda x: int(float(x)))

# Сохранение результата в новый CSV файл
output_file = 'sofas_prices_converted.csv'
df[['Цена']].to_csv(output_file, index=False)

print(f"Преобразованные данные сохранены в файл {output_file}")

# Чтение CSV файла
input_file = 'sofas_prices_converted.csv'
prices = pd.read_csv(input_file)
print(prices)

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(prices, bins=20, edgecolor='black')  # bins указывает количество корзин (интервалов)
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена')
plt.ylabel('Количество')
plt.grid(True)#Делаем сетку на фоне графика
# Отображение графика
plt.show()