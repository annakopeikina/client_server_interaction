import requests
import json

# Ваши учетные данные API
client_id = "__"
client_secret = "__"

# Конечная точка API
endpoint = "https://api.foursquare.com/v3/places/search"

# Определение параметров для запроса API
city = input("Введите название города: ")
place = input(" Destination: ")
params = {
    "client_id": client_id,
    "client_secret": client_secret,
    "near": city,
    "query": place
}

headers = {
    "Accept": "application/json",
    "Authorization": "fsq3brYSAxLWon225qRnWeMVlW4OwwpeO0Wc33YSMEo6W64="
}

# Отправка запроса API и получение ответа
response = requests.get(endpoint, params=params,headers=headers)

# Проверка успешности запроса API
if response.status_code == 200:
    print("Успешный запрос API!")
    data = json.loads(response.text)
    venues = data["results"]
    for venue in venues:
        print("Название:", venue["name"])
        print("Адрес:", venue["location"]["address"])
        print("\n")
else:
    print("Запрос API завершился неудачей с кодом состояния:", response.status_code)
    print(response.text)
