import matplotlib.pyplot as plt
import numpy as np

mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

data = np.random.normal(mean, std_dev, num_samples)
#Создаём гистограмму
plt.hist(data, bins=6)
plt.xlabel("ось X")
plt.ylabel("ось Y")
plt.title("Гистограмма")
plt.grid(True)#Делаем сетку на фоне графика
plt.show()

#random_array = np.random.rand(5)  # массив из 5 случайных чисел
#print(random_array)

x = np.random.rand(10)
y = np.random.rand(10)
print(x, y)
#Создаём диаграмму рассеивания
plt.scatter(x, y)
plt.xlabel("ось Х")
plt.ylabel("ось Y")
plt.title("диаграмма рассеяния")
plt.grid(True)#Делаем сетку на фоне графика
plt.show()