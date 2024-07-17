import requests
from lxml import html
import csv

# URL сайта
url = 'http://books.toscrape.com/'

# Отправка HTTP GET-запроса
response = requests.get(url, headers={
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    })
response.raise_for_status()  # Проверка успешности запроса

# Парсинг HTML-содержимого
tree = html.fromstring(response.content)

# XPath для извлечения данных из таблицы
books = tree.xpath('//article[@class="product_pod"]')

# Открытие CSV-файла для записи
with open('books.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Title', 'Price', 'Availability']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Извлечение данных и запись в CSV
    for book in books:
        title = book.xpath('.//h3/a/@title')[0]
        price = book.xpath('.//div[@class="product_price"]/p[@class="price_color"]/text()')[0]
        availability = book.xpath('.//div[@class="product_price"]/p[@class="instock availability"]/text()')[1].strip()
        writer.writerow({'Title': title, 'Price': price, 'Availability': availability})

print("Данные успешно сохранены в books.csv")