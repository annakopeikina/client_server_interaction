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

from lxml import html
import requests
import pandas as pd

# URL страницы с данными
url = 'https://www.google.com/analytics'

# Получаем содержимое страницы
response = requests.get(url)
page_content = html.fromstring(response.content)

# XPath для каждого столбца данных
xpath_columns = {
    'fixed acidity': './/div[@class="fixed_acidity"]/span/text()',
    'volatile acidity': './/div[@class="volatile_acidity"]/span/text()',
    'citric acid': './/div[@class="citric_acid"]/span/text()',
    'residual sugar': './/div[@class="residual_sugar"]/span/text()',
    'chlorides': './/div[@class="chlorides"]/span/text()',
    'free sulfur dioxide': './/div[@class="free_sulfur_dioxide"]/span/text()',
    'total sulfur dioxide': './/div[@class="total_sulfur_dioxide"]/span/text()',
    'density': './/div[@class="density"]/span/text()',
    'pH': './/div[@class="pH"]/span/text()',
    'sulphates': './/div[@class="sulphates"]/span/text()',
    'alcohol': './/div[@class="alcohol"]/span/text()',
    'quality': './/div[@class="quality"]/span/text()',
    'Type': './/div[@class="Type"]/text()'
}

# Список для хранения данных
data = []

# Итерируемся по каждому элементу данных
for col_name, xpath_expr in xpath_columns.items():
    # Извлекаем данные по XPath
    extracted_data = page_content.xpath(xpath_expr)
    # Преобразуем текстовое значение в число, если это возможно, или оставляем как есть
    extracted_data = [float(value) if value.replace('.', '', 1).isdigit() else value for value in extracted_data]
    # Добавляем данные в список
    data.append(extracted_data)

# Создаем DataFrame
df = pd.DataFrame(data, index=xpath_columns.keys()).T

# Выводим DataFrame
print(df)
