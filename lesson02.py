import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Список имен учеников
students = ['Алексей', 'Борис', 'Виктория', 'Дмитрий', 'Екатерина', 'Фёдор', 'Галина', 'Иван', 'Жанна', 'Константин']
# Список предметов
subjects = ['Математика', 'Физика', 'История', 'Литература', 'ИЗО']
# Генерация случайных оценок по пятибалльной системе (от 2 до 5)
np.random.seed(0)  # Для воспроизводимости результатов
grades = np.random.randint(2, 6, size=(10, 5))
# Создание DataFrame
data = {'Имя': students}
for i, subject in enumerate(subjects):
    data[subject] = grades[:, i]

df = pd.DataFrame(data)
IQR = df['Математика'].quantile(0.75) - df['Математика'].quantile(0.25)

# Печать DataFrame
print(df.head(5))
print(df.describe())
print(df.info())
print(f'Средний балл по каждому предмету:\n {df[subjects].mean()}')
print(f'Медианный балл по каждому предмету:\n {df[subjects].median()}')
print(f'стандартное отклонение для каждого предмета \n {df[subjects].std()}')
print(f'IQR - {IQR}')

df.boxplot(column='Математика')
plt.show()

df['Математика'].hist()
plt.show()
