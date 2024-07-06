import requests
import pandas as pd

# Ваши учетные данные АPI
client_id=""
client_secret = "__"

# Конечная точка АРΙ

endpoint = "https://api.foursquare.com/v3/places/search"

city = input('Введите название города: ')
place = input('Введите тип заведения: ')
params={
    'client_id': client_id,

    'client_secret': client_secret,
    'near': city,
    'query': place

 }

headers = {

    "Accept": "application/json",
    "Authorization": "fsq3brYSAxLWon225qRnWeMVlW4OwwpeO0Wc33YSMEo6W64="
}

response = requests.get(endpoint, params=params, headers=headers)
if response.status_code == 200:
    print("Success")
    data = response.json()
    venues = data['results']
   
    venues_data = []
    for venue in venues:
        name = venue["name"]
        address = venue.get("location", {}).get("address", "Адрес не указан")
       
        venues_data.append({"Название": name, "Адрес": address})

    df = pd.DataFrame(venues_data)
    print(df.head())
else:
    print("Failed to get data:", response.status_code)
    print(response.text)