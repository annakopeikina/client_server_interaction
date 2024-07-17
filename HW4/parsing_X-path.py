import requests
from lxml import html
import pandas as pd

url = "https://www.worldathletics.org/records/toplists/sprints/60-metres/indoor/women/senior/2023?page=1"

response = requests.get(url, headers={
'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'})

# https://pypi.org/project/fake-useragent/

tree = html.fromstring(response.content)
# print(tree)

table_rows = tree.xpath("//table[@class='records-table']/tbody/tr")
list_data = []
for row in table_rows:
    columns = row.xpath(".//td/text()")
    list_data.append({
        'Rank': columns[0].strip(),
        'Mark': columns[1].strip(),
        'WIND': columns[2].strip(),
        'Competitor': row.xpath(".//td[4]/a/text()")[0].strip(),
        'DOB': columns[5].strip(),
        'Nat': columns[7].strip(),
        'Pos': columns[8].strip(),
        'Venue': columns[9].strip(),
        'Date': columns[10].strip(),
        'Results_Store': columns[11].strip(),   
    })
 
df = pd.DataFrame(list_data)   
print(df)