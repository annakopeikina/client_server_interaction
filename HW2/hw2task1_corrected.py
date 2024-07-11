# Выполнить скрейпинг данных в веб-сайта http://books.toscrape.com/ и извлечь информацию 
# о всех книгах на сайте во всех категориях: название, цену, количество товара в наличии 
# (In stock (19 available)) в формате integer, описание.

import requests
from bs4 import BeautifulSoup
import json
    
base_url = 'http://books.toscrape.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.67 Safari/537.36'}
    
all_books = []
    
def scrape_books_in_category(category_url, headers):
    books_data = []
    while category_url:
        response = requests.get(category_url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        products = soup.find_all('article', class_='product_pod')
    
        for product in products:
            book_url = base_url + product.find('h3').find('a')['href'].replace('../../../', 'catalogue/')
            books_data.append(get_book_info(book_url, headers))
    
        next_button = soup.find('li', class_='next')
        if next_button:
            next_page = next_button.find('a')['href']
            category_url = '/'.join(category_url.split('/')[:-1]) + '/' + next_page
        else:
            category_url = None
    
    return books_data
    
def get_book_info(book_url, headers):
    response = requests.get(book_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('h1').text.strip()
    price = soup.find('p', class_='price_color').text.strip().replace('£', '')
    availability = soup.find('p', class_='instock availability').text.strip()
    availability = int(''.join(filter(str.isdigit, availability)))
    description_tag = soup.find('meta', attrs={'name': 'description'})
    description = description_tag['content'].strip() if description_tag else 'No description available.'
    
    book_info = {
        'Title': title,
        'Price': float(price),
        'Availability': availability,
        'Description': description
    }
    return book_info
    
response = requests.get(base_url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
categories = soup.find('ul', class_='nav-list').find('ul').find_all('a')
for category in categories:
    category_url = base_url + category['href']
    print(f"Scraping category URL: {category_url}")
    all_books.extend(scrape_books_in_category(category_url, headers))
    
with open('books_data.json', 'w', encoding='utf-8') as f:
    json.dump(all_books, f, ensure_ascii=False, indent=4)
    
print("Data has been scraped and saved to books_data.json")