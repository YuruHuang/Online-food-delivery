import scrapy
import pandas as pd
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from scrapy import Selector
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import json 



class UbereatsAddressSpider(scrapy.Spider):
    name = 'UberEats_address'
    allowed_domains = ['ubereats.com']
    start_urls = ['https://www.ubereats.com/gb/feed?ad_id=619145546147&campaign_id=18201757191&diningMode=DELIVERY&gclid=Cj0KCQjwk7ugBhDIARIsAGuvgPb5dCh2zzD0zxFIRgJiS7qfdcV7qDbLj_oIFEBxpuwnVRhzwJdD3uQaAmyCEALw_wcB&gclsrc=aw.ds&kw=uber%20eats&kwid=kwd-111378724137&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMkNCMiUyMDFEUSUyMiUyQyUyMnJlZmVyZW5jZSUyMiUzQSUyMkNoSUplMW0tNXBsdzJFY1JlY29qZWZ4V1pPdyUyMiUyQyUyMnJlZmVyZW5jZVR5cGUlMjIlM0ElMjJnb29nbGVfcGxhY2VzJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0E1Mi4yMDE0MTgyJTJDJTIybG9uZ2l0dWRlJTIyJTNBMC4xMjUxNjUyJTdE&placement=&ps=1&utm_campaign=CM2199893-search-google-brand_1_-99_US-National_e_web_acq_cpc_en_T1_Generic_BM_uber%20eats_kwd-111378724137_619145546147_140206624749_b_c&utm_source=AdWords_Brand']


    def __init__(self):
        chrome_service = Service(executable_path='C:\\Users\\yh459\\PycharmProjects\\UberEats(forJody)\\chromedriver.exe')
        self.driver = webdriver.Chrome(service= chrome_service)
    
    def parse(self, response):
        urls = pd.read_csv('UberEats_GB_postcodes2_unique.csv')['restaurant url']
        i=0
        for url in urls[31:]:
            print(i)
            i+=1
            self.driver.get(url)
            sleep(5)
            # driver.find_element(By.XPATH,"//a[@class='ba bt bb bu c5 ah am bf bc ja dk b0 ax c6 c7 c8 bn bo']").click()
            try:
                page = Selector(text = self.driver.page_source)
                txt = page.xpath('//script[@id="__REDUX_STATE__"]/text()').get()
                txtNew = txt.encode('utf-8').decode('unicode_escape','surrogatepass').replace('\n','').strip().replace('%5C"','\'')
                json_geo = json.loads(txtNew)
                json_dat = json.loads(page.xpath('//main[@id="main-content"]/script[@type="application/ld+json"]/text()').get())
                with open('ubereats JSON IFPS/ubereats'+str(i)+'.json', 'w') as f:
                    json.dump(json_dat, f)
                key = list(json_geo.get('stores').keys())[0]
                store = json_geo.get('stores').get(key).get('data').get('location')
                yield{
                        'URL': url,
                        'Type': json_dat.get('@type'),
                        'Name': json_dat.get('name'),
                        'Latitude': store.get('latitude'),
                        'Longitude': store.get('longitude'),
                        'Address': store.get('address'), 
                        'Cuisine Type': json_dat.get('servesCuisine'),
                        'Price Range': json_dat.get('priceRange'),
                        'Aggregated Rating': json_dat.get('aggregateRating').get('ratingValue'),
                        'Review Number': json_dat.get('aggregateRating').get('reviewCount')
                    }
            except:
                print('not working')

