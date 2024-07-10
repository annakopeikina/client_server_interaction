import requests
from bs4 import BeautifulSoup
import urllib.parse
from datetime import datetime
import time
import re
import json

def get_box_office_data():
    url = 'https://www.boxofficemojo.com/intl/?ref_=bo_nb_hm_tab'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    release_links = []
    for link in soup.find_all('td', class_='a-text-left mojo-field-type-release mojo-cell-wide'):
        a_tag = link.find('a')
        if a_tag:
            release_links.append(a_tag.get('href'))

    url_joined = [urllib.parse.urljoin('https://www.boxofficemojo.com', link) for link in release_links]

    data = []
    for url in url_joined:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('div', class_='a-section a-spacing-none mojo-summary-values mojo-hidden-from-mobile')

        if not table:
            continue

        rows = table.find_all('div', class_='a-section a-spacing-none')

        row_data = {}
        for row in rows:
            key = row.find('span').text.strip()
            spans = row.find_all('span')
            if len(spans) > 1:
                value = spans[1].text.strip()
                if key == 'Opening':
                    value = int(re.sub('[^0-9]', '', value))
                elif key == 'Release Date':
                    value = value
                elif key == 'Running Time':
                    try:
                        time_parts = re.findall(r'\d+', value)
                        hours, minutes = map(int, time_parts)
                        value = hours * 3600 + minutes * 60
                    except ValueError:
                        continue
                elif key == 'Genres':
                    value = [genre.strip() for genre in value.split(',') if genre.strip()]
                elif key == 'In Release':
                    value = re.sub(r'[^\d]', '', value)
                elif key == 'Widest Release':
                    value = int(re.sub('[^0-9]', '', value))

                row_data[key] = value

        if row_data:
            data.append(row_data)
        # time.sleep(1)

    return data

def save_data_to_json(data, filename='box_office_data.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def main():
    data = get_box_office_data()
    save_data_to_json(data)

if __name__ == "__main__":
    main()