import requests
import pandas as pd
from lxml import html

url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
response = requests.get(url, headers={
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
})
response.raise_for_status()

tree = html.fromstring(response.content)
table = tree.xpath('//table[contains(@class, "wikitable")][1]')
df = pd.read_html(html.tostring(table[0]))[0]
df.to_csv('countries_population.csv', index=False)

print("Данные успешно сохранены в countries_population.csv")