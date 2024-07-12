from pymongo import MongoClient
import json
import os

# Подключение к MongoDB через UNIX-сокет
client = MongoClient('mongodb://localhost:27017/')

# Выбор базы данных и коллекции
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
