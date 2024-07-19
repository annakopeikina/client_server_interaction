# Выберите веб-сайт с табличными данными, который вас интересует.
# Напишите код Python, использующий библиотеку requests для отправки HTTP GET-запроса на сайт и получения HTML-содержимого страницы.
# Выполните парсинг содержимого HTML с помощью библиотеки lxml, чтобы извлечь данные из таблицы.
# Сохраните извлеченные данные в CSV-файл с помощью модуля csv.

# Ваш код должен включать следующее:

# Строку агента пользователя в заголовке HTTP-запроса, чтобы имитировать веб-браузер и избежать блокировки сервером.
# Выражения XPath для выбора элементов данных таблицы и извлечения их содержимого.
# Обработка ошибок для случаев, когда данные не имеют ожидаемого формата.
# Комментарии для объяснения цели и логики кода.

# Примечание: Пожалуйста, не забывайте соблюдать этические и юридические нормы при веб-скреппинге.
# https://f inance.yahoo.com/trending-tickers/
# Сайты для парсинга таблиц.
# https://www.worldometers.info/
# imdb
# https://finance.yahoo.com/trending-tickers/
# https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)
# https://proxyway.com/guides/best-websites-to-practice-your-web-scraping-skills
# Интересные апи
# https://kinopoisk.dev/
# https://openweathermap.org/api
# Датасеты в неограниченном количестве
# https://www.kaggle.com/

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# Путь к chromedriver
chromedriver_path = "C:/Users/annav/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"

# Настройка опций Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Запуск в фоновом режиме
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Инициализация драйвера
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL страницы с данными
url = 'https://www.kaggle.com/datasets/anoopjohny/comprehensive-drug-information-dataset'
driver.get(url)

# Ожидание загрузки страницы
time.sleep(10)  # Увеличьте время, если страница загружается медленно

# Поиск элементов
elements = driver.find_elements(By.XPATH, '//div[contains(@class, "sc-dtiVSR gpTZlZ") or contains(@class, "sc-hEXWOQ sc-hkBrTZ eINUbH jjuHDA")] | //span[contains(@class, "sc-euGpHm kYvmjp")]')

if not elements:
    driver.quit()
    raise ValueError("Не удалось найти элементы с заданными классами")

# Извлечение данных
data = []
for element in elements:
    data.append([e.text for e in element.find_elements(By.XPATH, './div')])

# Закрытие драйвера
driver.quit()

# Создание DataFrame
columns = ['Drug ID', 'Drug Name', 'Generic Name', 'Drug Class', 'Indication']
df = pd.DataFrame(data, columns=columns)

# Сохранение в CSV
df.to_csv('drug_information.csv', index=False)

print("Данные успешно сохранены в drug_information.csv")
