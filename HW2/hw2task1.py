# Выполнить скрейпинг данных в веб-сайта http://books.toscrape.com/ и извлечь информацию 
# о всех книгах на сайте во всех категориях: название, цену, количество товара в наличии 
# (In stock (19 available)) в формате integer, описание.

from bs4 import BeautifulSoup
import requests
import urllib.parse
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

url = 'http://books.toscrape.com/'
response = requests.get(url, headers=headers)

print(f"Status code: {response.status_code}")

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    category_links = []
    for link in soup.find_all('a', href=True):
        full_url = urllib.parse.urljoin(url, link['href'])
        if full_url not in category_links and 'catalogue/category/books/' in full_url:
            category_links.append(full_url)

    print(f"Found {len(category_links)} category links.")

    titles = []
    prices = []
    availability = []
    descriptions = []

    for category_link in category_links:
        response = requests.get(category_link, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            for book in soup.find_all('article', class_='product_pod'):
                title = book.h3.a['title']
                titles.append(title)
                
                price_str = book.find('p', class_='price_color').text.strip('Â£')
                price = float(price_str[1:]) 
                prices.append(price)
                
                availability_str = book.find('p', class_='instock availability').text.strip()
                availability_words = availability_str.split()
                if len(availability_words) > 2:
                    availability_number = int(availability_words[2])
                else:
                    availability_number = 0  
                availability.append(availability_number)
                
                descriptions.append("No description available")

    data = {
        'Title': titles,
        'Price': prices,
        'Availability': availability,
        'Description': descriptions
    }
    df = pd.DataFrame(data)

    print(df)

    df.to_json('books_data.json', orient='records', indent=4)
else:
    print("Failed to fetch the main page. Please check the URL or your internet connection.")
