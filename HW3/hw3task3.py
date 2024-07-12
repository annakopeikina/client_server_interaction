from pymongo import MongoClient
import json
import os

# Подключение к MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['HW2']
collection = db['books']

# Путь к файлу JSON с данными
json_filename = r'C:\Users\annav\OneDrive\Desktop\client_server_interaction\HW2\books_data.json'

# Проверка существования файла
if os.path.exists(json_filename):
    # Загрузка данных из JSON файла в MongoDB
    with open(json_filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        collection.insert_many(data)
    print("Данные успешно загружены в MongoDB.")
else:
    print(f"Файл {json_filename} не найден.")

# Функция для подсчета числа записей по запросу и вывода результата
def count_documents(query, message):
    count = collection.count_documents(query)
    print(f"{message}: {count}")

# Примеры запросов с подсчетом

# 1. Подсчет книг с ценой больше 8
price_greater_than_8_query = {'Price': {'$gt': 8}}
count_documents(price_greater_than_8_query, "Количество книг с ценой больше 8")

# 2. Подсчет книг, у которых в названии содержится слово 'moon'
moon_in_title_query = {'Title': {'$regex': 'moon', '$options': 'i'}}
count_documents(moon_in_title_query, "Количество книг, в названии которых есть 'moon'")

# 3. Комбинированный запрос: книги с ценой больше 8 и в названии содержится 'moon'
combined_query = {'Price': {'$gt': 8}, 'Title': {'$regex': 'moon', '$options': 'i'}}
count_documents(combined_query, "Количество книг с ценой больше 8 и в названии есть 'moon'")

# 4. Другие примеры запросов с подсчетом можно добавить по аналогии

# Закрытие соединения с MongoDB
client.close()
