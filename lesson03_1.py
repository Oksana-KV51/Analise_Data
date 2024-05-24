import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Настройки для запуска браузера
options = Options()
options.headless = True  # Запуск браузера в фоновом режиме

# Установка драйвера для Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# URL сайта, который будем парсить
url = 'https://www.divan.ru/category/divany'

# Открываем страницу
driver.get(url)
time.sleep(5)  # Ожидание загрузки страницы

# Получаем информацию о диванах
sofas = driver.find_elements(By.CLASS_NAME, 'WdR1o')

data = []
for sofa in sofas:
    try:
        # Название дивана
        title = sofa.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text
        # Цена дивана
        price = sofa.find_element(By.CSS_SELECTOR, 'meta[itemprop="price"]').get_attribute('content')
        data.append([title, price])
    except Exception as e:
        print(f"Ошибка при обработке элемента: {e}")

# Закрываем браузер
driver.quit()

# Сохранение данных в CSV файл
csv_file = 'sofas_prices.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена'])
    writer.writerows(data)

print(f"Данные сохранены в файл {csv_file}")




