 # Используйте операторы $lt и $gte для подсчета количества документов с "properties.month" меньше 6 и больше или равно 6,
 # соответственно.
#- Используйте оператор $regex для подсчета количества документов, содержащих слово "rain" в поле "properties.weather",
# игнорируя регистр.
#- Используйте оператор $in для подсчета количества документов, в которых "properties.rdclass" является либо "US ROUTE",
# либо "STATE SECONDARY ROUTE".
#- Используйте оператор $all для подсчета количества документов, в которых "properties.rdconfigur" содержит как "TWO-WAY",
# так и "DIVIDED".
#- Используйте оператор $ne для подсчета количества документов, у которых "properties.rdcondition" не равно "DRY".


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
for doc in projection:
    print(doc)
    
query = {'properties.month': {'$lt': 6, '$gte': 6}}