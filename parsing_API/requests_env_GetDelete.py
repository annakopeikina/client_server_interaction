# request
import requests
response = requests.get('http://jsonplaceholder.typicode.com/posts/1')
if response.status_code == 200:
    print('Vashradande Demble!')
    print(response.text)
else:
    print('Vashradande Demble is not what you expect:', response.status_code)
    
# post request  
data = {
    'title': 'GeekBrains',
    'body': 'Scraping',
    'userID': 1
}  

response = requests.post('http://jsonplaceholder.typicode.com/posts/1', json = data)

if response.status_code == 201:
    print('Vashradande Demble!')
    print(response.text)
else:
    print('Vashradande Demble is not what you expect:', response.status_code)
    

# put
payload = {'field1': 'value1', 'field2': 'value2'}
response = requests.put('http://jsonplaceholder.typicode.com/posts/1', json = payload)

if response.status_code == 200:
    print('Vashradande Demble!')
    print(response.text)
else:
    print('Vashradande Demble is not what you expect:', response.status_code)
