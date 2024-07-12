#- Установите пакет PyMongo и импортируйте MongoClient и json.
#- Установите Compass MongoDB
#- Подключитесь к серверу MongoDB по адресу 'mongodb://localhost:27017/'.
#- Создайте базу данных 'town_cary' и коллекцию 'crashes'.
#- Выполните чтение файла JSON 'crash-data.json'.
#- Напишите функцию chunk_data, которая принимает два аргумента: список данных и размер фрагмента. 
#       Функция должна разделить данные на более мелкие фрагменты указанного размера и вернуть генератор.
#- Разделите данные JSON на фрагменты по 5000 записей в каждом.
#- Переберите все фрагменты и вставьте каждый фрагмент в коллекцию MongoDB с помощью функции insert_many().
#- Выведите финальное сообщение, указывающее на то, что данные были успешно вставлены.

import json
from pymongo import MongoClient

# подключение к серверу MangoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['town_cary'] 

collection = db['crashes']

with open('HW3/crash-data.json', 'r') as file:
    data = json.load(file)

data = data['features']

def chank_data(data, chank_size):
    for i in range(0, len(data),chank_size):
        yield data[i:i+chank_size]
chank_size = 5000
data_chank = list(chank_data(data, chank_size))

for chank in data_chank:
    collection.insert_many(chank)
    
for chank in data_chank:
    collection.insert_many(chank)