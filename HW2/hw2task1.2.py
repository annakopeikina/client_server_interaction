from bs4 import BeautifulSoup
import requests
import urllib.parse
import pandas as pd

url = 'http://books.toscrape.com/catalogue/category/books/'
response = requests.get(url)

# Check the status code
print(f"Status code: {response.status_code}")

soup = BeautifulSoup(response.content, 'html.parser')

# Find all links to book categories
category_links = []
for link in soup.find_all('a', href=True):
    category_links.append(urllib.parse.urljoin(url, link['href']))

print(f"Found {len(category_links)} category links.")

# Initialize empty lists to store data
titles = []
prices = []
availability = []
descriptions = []

# Loop through each category link to scrape book data
for category_link in category_links:
    response = requests.get(category_link)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract data from each book in the category
    for book in soup.find_all('article', class_='product_pod'):
        # Title
        title = book.h3.a['title']
        titles.append(title)
        
        # Price
        price = book.find('p', class_='price_color').text.strip('Â')
        prices.append(price)
        
        # Availability
        availability_str = book.find('p', class_='instock availability').text.strip()
        availability.append(int(availability_str.split()[0]))
        
        # Description
        description = book.find('p', class_='').text.strip()
        descriptions.append(description)

# Create a DataFrame from the scraped data
data = {
    'Title': titles,
    'Price': prices,
    'Availability': availability,
    'Description': descriptions
}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
