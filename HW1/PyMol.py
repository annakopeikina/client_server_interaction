import requests

url = "https://data.rcsb.org/rest/v1/core/entry/4HHB"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
