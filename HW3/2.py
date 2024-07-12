from pymongo import MongoClient
import json

client = MongoClient()
db = client['town_cary']
collection = db['crashes']


# вывод первой записи в коллекции
all_docs = collection.find()
first_doc = all_docs[0]


# вывод объекта json
pretty_json = json.dumps(first_doc, indent=4, default=str)
print(pretty_json)

# cоunter

count = collection.count_documents({})
print(f"число записей в базе данных = {count}")
query =  {'properties.fatalities': 'Yes'}
print(f'Количество документов с погибшими: {collection.count_documents(query)}')

projection = {'properties.lightcond':1, 'properties.weather':1,'_id':0}
project = collection.find(query, projection)
for doc in project:
    print(doc)
    
query = {'properties.month': {'$lt':'6', }}
print(f'Количество аварий за период менее 6 месяцев: {collection.count_documents(query)}')

query = {'properties.month': {'$gte':'6', }}
print(f'Количество аварий за период более 6 месяцев: {collection.count_documents(query)}')

query = {'properties.weather': {'$regex':'rain', '$options': 'i'}}
print(f'Количество аварий во время дождя: {collection.count_documents(query)}')

query = {'properties.rdclass': {'$in': ['US ROUTE', "STATE SECONDARY ROUTE"]}}
print(f'Количество аварий на US ROUTE или STATE SECONDARY ROUTE: {collection.count_documents(query)}')

query = {'properties.rdconfigur': {'$all': ['TWO-WAY', "DIVIDED"]}}
print(f'Количество аварий на TWO-WAY или DIVIDED: {collection.count_documents(query)}')

query = {'properties.rdcondition': {'$ne': 'DRY'}}
print(f'Количество аварий не на DRY: {collection.count_documents(query)}')