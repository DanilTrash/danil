import requests
import bs4
import scrapy
urls = open(r'C:\Users\KIEV-COP-4\Desktop\danil\soderjanki\all_urls.txt').read().splitlines()


class SoderjankaParserSpider(scrapy.Spider):
    name = 'soderjanka_parser'
    allowed_domains = ['www.soderganki.ru']
    start_urls = urls
    custom_settings = {'FEED_URI': "extrcd_data.json",
                       'FEED_FORMAT': 'json'}

    def parse(self, original_resp):
        hrefs = original_resp.xpath('/html/body/div[1]/div[3]/div/h4/a/@href').extract()
        for href in hrefs:
            resp = requests.get(href)
            soup = bs4.BeautifulSoup(resp.text, 'lxml')
            h1 = soup.find('h1')
            div = soup.find('div', {'class': 'entry'})
            return_Data = {
                'page': original_resp.url,
                'href': href,
                'data': {
                    'h1': h1.text,
                    'div': {
                        f'p{i}': p.text for i, p in enumerate(div.find_all('p'), 1)
                    }}
            }
            yield return_Data
