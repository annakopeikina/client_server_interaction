import scrapy

class CountriesSpiderSpider(scrapy.Spider):
    name = "countries_spider"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_sovereign_states"]

    def parse(self, response):
        rows = response.xpath('//table[contains(@class,"wikitable")][1]/tbody/tr')
        for row in rows:
            country_name = row.xpath('.//td[1]//a/text()').get()
            membership = row.xpath('.//td[contains(.,"UN")]/text()').get()
            sovereignity_dispute_info = row.xpath('.//td[3]/text()').get()
            country_status = row.xpath('.//td[4]/text()').get()
                                   
            link = row.xpath(".//b/a/@href").get()
            yield response.follow(url=link if link else '/wiki/Zambia', callback=self.parse_country, 
                                  meta={
                                      'country': country_name,
                                      'membership': membership,
                                      'sovereignity_dispute_info': sovereignity_dispute_info,
                                      'country_status': country_status
                                  })         
    
    def parse_country(self, response):
        rows = response.xpath("//table[contains(@class,'infobox ib-country vcard')][1]/tbody")
        for row in rows:
            capital = response.xpath('//th[contains(text(),"Capital")]/following-sibling::td[1]/a/text()').get()
            country_name = response.request.meta['country']
            membership = response.request.meta['membership']
            sovereignity_dispute_info = response.request.meta['sovereignity_dispute_info']
            country_status = response.request.meta['country_status']
                
            yield {
                'country_name': country_name.strip() if country_name else '',
                'capital': capital.strip() if capital else '',
                'membership': membership.strip() if membership else '',
                'sovereignty_dispute_info': sovereignity_dispute_info.strip() if sovereignity_dispute_info else '',
                'country_status': country_status.strip() if country_status else ''
            }
