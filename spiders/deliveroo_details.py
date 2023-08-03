import scrapy
from scrapy import Selector
import pandas as pd
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import json


class DeliverooDetailsSpider(scrapy.Spider):
    name = 'deliveroo_details'
    allowed_domains = ['deliveroo.co.uk']
    start_urls = ['https://deliveroo.co.uk/']

    def __init__(self):
        chrome_service = Service(
            executable_path='C:\\Users\\yh459\\PycharmProjects\\UberEats(forJody)\\chromedriver.exe')
        self.driver = webdriver.Chrome(service=chrome_service)

    def parse(self, response):
        urls = pd.read_csv('../Deliveroo_IFPS_URLS_unique.csv')['restaurant url']
        i=61803
        for url in urls[61803:]: 
            print(i)
            i+=1
            self.driver.get(url)
            sleep(5)
            try:
                page = Selector(text = self.driver.page_source)
                json_dat = json.loads(page.xpath('//script[@id="__NEXT_DATA__"]/text()').get())
                with open('Deliveroo JSON IFPS/deliveroo'+str(i)+'.json', 'w') as f:
                    json.dump(json_dat, f)     
# with open('ubereats/Deliveroo JSON IFPS/deliveroo13402.json') as f:
#     json_str = f.read()
# json_dat = json.loads(json_str)
                restaurant  = json_dat.get('props').get('initialState').get('menuPage').get('menu').get('meta').get('restaurant')
                cuisines = page.xpath('//div[@class="UILines-eb427a2507db75b3 ccl-2d0aeb0c9725ce8b ccl-45f32b38c5feda86"][1]/span[@class="ccl-649204f2a8e630fd ccl-a396bc55704a9c8a ccl-0956b2f88e605eb8"]/text()').getall()
                address_list = list(restaurant.get('location').get('address').values())
                yield{
                        'URL': url,
                        'id': restaurant.get('id'),
                        'Name':restaurant.get('name'),
                        'Address': ', '.join([ad for ad in address_list if ad is not None]),
                        'Cuisines': cuisines
                    }
            except:
                print('not working')


# adding i+20945