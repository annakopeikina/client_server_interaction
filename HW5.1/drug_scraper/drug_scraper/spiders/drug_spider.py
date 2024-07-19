# import scrapy


# class DrugSpiderSpider(scrapy.Spider):
#     name = "drug_spider"
#     allowed_domains = ["ru.wikipedia.org"]
#     start_urls = ['https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D0%BD%D1%8B%D0%B9_%D0%BF%D0%B5%D1%80%D0%B5%D1%87%D0%B5%D0%BD%D1%8C_%D0%92%D0%9E%D0%97_%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D1%85_%D0%BB%D0%B5%D0%BA%D0%B0%D1%80%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%8B%D1%85_%D1%81%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B2']
    
#     def parse(self, response):
#             rows = response.xpath('.//table[contains(@class,"wikitable")[4]/tbody/tr[1]')
#             for row in rows:
#                 drug = row.xpath('.//tr/td[1]/text()').get()
#                 prescriptions = row.xpath('/tr/td[2]/text()').get()

#                 link = row.xpath('.//td[1]/a/@href').get()
#                 if link:
#                     link = response.urljoin(link)
                    
#                 yield response.follow(url=link, callback=self.parse_drug,
#                                     meta={
#                                         'Препарат': drug,
#                                         'Показания': prescriptions,
#                                     })

#     def parse_drug(self, response):
#         drug = response.request.meta['Препарат']
#         prescriptions = response.request.meta['Показания']

#         yield {
#             'Препарат': drug.strip() if drug else '',
#             'Показания': prescriptions.strip() if prescriptions else '',
#         }
# import scrapy

# class DrugSpider(scrapy.Spider):
#     name = "drug_spider"
#     allowed_domains = ["ru.wikipedia.org"]
#     start_urls = ["https://ru.wikipedia.org/wiki/Примерный_перечень_ВОЗ_основных_лекарственных_средств"]

#     def parse(self, response):
#         rows = response.xpath('//table[contains(@class,"wikitable")][4]/tbody/tr')
#         for row in rows[1:]:  # Пропускаем заголовок таблицы
#             drug = row.xpath('.//td[1]/a/text()').get()
#             prescriptions = row.xpath('.//td[2]/text()').get()
#             link = row.xpath('.//td[1]/a/@href').get()

#             if link:
#                 link = response.urljoin(link)
#                 yield response.follow(url=link, callback=self.parse_drug,
#                                       meta={
#                                           'drug': drug,
#                                           'prescriptions': prescriptions
#                                       })
#             else:
#                 yield {
#                     'drug': drug,
#                     'prescriptions': prescriptions,
#                     'link': None
#                 }

#     def parse_drug(self, response):
#         drug = response.meta['drug']
#         prescriptions = response.meta['prescriptions']
#         additional_info = response.xpath('//div[@class="mw-parser-output"]//text()').getall()
        
#         yield {
#             'drug': drug,
#             'prescriptions': prescriptions,
#             'additional_info': ' '.join(additional_info)
#         }

# import scrapy

# class DrugSpiderSpider(scrapy.Spider):
#     name = "drug_spider"
#     allowed_domains = ["ru.wikipedia.org"]
#     start_urls = ["https://ru.wikipedia.org/wiki/Примерный_перечень_ВОЗ_основных_лекарственных_средств"]

#     def parse(self, response):
#         rows = response.xpath('/html/body/div[3]/div[3]/div[5]/div[1]/table[4]/tbody/tr')
#         for row in rows:
#             # Отладочная информация
#             drug = row.xpath('td[1]//text()').getall()
#             indications = row.xpath('td[2]//text()').getall()
#             self.log(f"Drug: {drug}")
#             self.log(f"Indications: {indications}")
            
#             # Основной код
#             drug = ' '.join(drug).strip()
#             indications_str = ', '.join([text.strip() for text in indications if text.strip()]).strip()
#             yield {
#                 'Препарат': drug,
#                 'Показания': indications_str
#             }

# import scrapy

# class DrugSpiderSpider(scrapy.Spider):
#     name = 'drug_spider'
#     start_urls = ['https://ru.wikipedia.org/wiki/Примерный_перечень_ВОЗ_основных_лекарственных_средств']

#     def parse(self, response):
#         # Извлечение текста из <a> тега внутри <td> и игнорирование <sup>
#         rows = response.xpath('//td')
#         for row in rows:
#             name = row.xpath('.//a/text()').get()
#             if name:
#                 yield {'name': name}

import scrapy

class DrugSpiderSpider(scrapy.Spider):
    name = 'drug_spider'
    allowed_domains = ['ru.wikipedia.org']
    start_urls = ['https://ru.wikipedia.org/wiki/Примерный_перечень_ВОЗ_основных_лекарственных_средств']

    def parse(self, response):
        # Получаем строки таблицы
        rows = response.xpath('.//table[contains(@class,"wikitable")][1]/tbody/tr')
        
        # Пропускаем первую строку (заголовки таблицы)
        for row in rows[1:]:
            # Получаем ячейки строки
            cells = row.xpath('td')
            if len(cells) > 1:
                # Извлекаем данные из ячеек
                drug = cells[0].xpath('a/text()').get()
                indications = cells[1].xpath('text()').get()
                
                # Выводим данные
                yield {
                    'Препарат': drug,
                    'Показания': indications,
                }
    def parse(self, response):
        for row in response.xpath('//xpath-to-table-row'):
            yield {
                'Препарат': row.xpath('.//xpath-to-drug/text()').get(),
                'Показания': row.xpath('.//xpath-to-indication/text()').get()
            }

