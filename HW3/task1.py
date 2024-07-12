from pymongo import MongoClient
import json

# Подключение к MongoDB
client = MongoClient('mongodb://localhost:27017')
database = client['HW3']
collection = database['1']

# Получение всех документов из коллекции
outdocs = list(collection.find())

if outdocs:
    first_doc = outdocs[0]
    json_lib = json.dumps(outdocs, indent=4, default=str)
    print(json_lib)
else:
    print("Коллекция пуста или не удалось получить документы.")
