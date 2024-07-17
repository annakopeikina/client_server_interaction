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

import requests
from lxml import html
import pandas as pd

# URL страницы с данными о разрешенных лекарствах на сайте FDA
url = "https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm"

try:
    # Отправка HTTP GET запроса с заданным User-Agent для имитации браузера
    response = requests.get(url, headers={
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    })

    # Проверка успешности запроса
    response.raise_for_status()

    # Парсинг HTML содержимого страницы
    tree = html.fromstring(response.content)

    # Извлечение данных о лекарствах
    drugs = []
    rows = tree.xpath("//table[@class='dataTable']/tbody/tr")
    for row in rows:
        name = row.xpath(".//td[@headers='brandName']/a/text()")
        active_ingredient = row.xpath(".//td[@headers='activeIngredient']/text()")
        dosage_form = row.xpath(".//td[@headers='dosageForm']/text()")
        company = row.xpath(".//td[@headers='applicant']/text()")

        # Проверка наличия данных перед добавлением в список
        if name and active_ingredient and dosage_form and company:
            drugs.append({
                'Name': name[0].strip(),
                'Active Ingredient': active_ingredient[0].strip(),
                'Dosage Form': dosage_form[0].strip(),
                'Company': company[0].strip()
            })

    # Создание DataFrame с извлеченными данными
    df = pd.DataFrame(drugs)

    # Сохранение DataFrame в CSV файл
    csv_filename = 'fda_approved_drugs.csv'
    df.to_csv(csv_filename, index=False)

    print(f"Данные успешно извлечены и сохранены в файл: {csv_filename}")

except requests.exceptions.RequestException as e:
    print(f"Произошла ошибка при выполнении HTTP запроса: {e}")

except Exception as e:
    print(f"Произошла ошибка при выполнении скрипта: {e}")
