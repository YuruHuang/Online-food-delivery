import scrapy
import pandas as pd
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from scrapy import Selector
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Ubereats2Spider(scrapy.Spider):
    name = 'UberEATS2'
    allowed_domains = ['ubereats.com']
    start_urls = ['https://www.ubereats.com/gb']


    def __init__(self):
        self.driver = webdriver.Chrome('C:\\Users\\yh459\\PycharmProjects\\UberEats(forJody)\\chromedriver.exe')

    def parse(self, response):
        # postcodes = pd.read_excel('V:\\P8_PHI\\DPH\\Yuru Huang\\UberEats(forJody)\\IFPS 2023\\Uber Eats scrape.xlsx')['PC']
        postcodes = ['SW1P 4PR', 'BT52 1TZ']
        i=0
        for postcode in postcodes:
            print(i)
            i+=1
            self.driver.get(
                "https://www.ubereats.com/gb/feed?diningMode=DELIVERY&mod=locationManager&modctx=feed&next=%2Fgb%2Ffeed%3FdiningMode%3DDELIVERY%26pl%3DJTdCJTIyYWRkcmVzcyUyMiUzQSUyMkNCMiUyMDFEUSUyMiUyQyUyMnJlZmVyZW5jZSUyMiUzQSUyMkNoSUplMW0tNXBsdzJFY1JlY29qZWZ4V1pPdyUyMiUyQyUyMnJlZmVyZW5jZVR5cGUlMjIlM0ElMjJnb29nbGVfcGxhY2VzJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0E1Mi4yMDE0MTgyJTJDJTIybG9uZ2l0dWRlJTIyJTNBMC4xMjUxNjUyJTdE%26ps%3D1&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMkNCMiUyMDFEUSUyMiUyQyUyMnJlZmVyZW5jZSUyMiUzQSUyMkNoSUplMW0tNXBsdzJFY1JlY29qZWZ4V1pPdyUyMiUyQyUyMnJlZmVyZW5jZVR5cGUlMjIlM0ElMjJnb29nbGVfcGxhY2VzJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0E1Mi4yMDE0MTgyJTJDJTIybG9uZ2l0dWRlJTIyJTNBMC4xMjUxNjUyJTdE&ps=1")
            sleep(5)
            # driver.find_element(By.XPATH,"//a[@class='ba bt bb bu c5 ah am bf bc ja dk b0 ax c6 c7 c8 bn bo']").click()
            self.driver.find_element(By.ID, "location-typeahead-location-manager-input").send_keys(postcode)
            sleep(2)
            elements = self.driver.find_elements(By.XPATH, "//ul[@id='location-typeahead-location-manager-menu']/li")
            if [] == elements:
                pass
            else:
                self.driver.execute_script("arguments[0].click();", elements[0])
                sleep(5)
            # show more
            show_more = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Show more')]")
            while len(show_more)!=0:
                # if click 'show more' gives your awkward taco
                try:
                    self.driver.find_element(By.XPATH,'//a[@href="/gb/taco-bout-awkward"]')
                    break
                except:
                    self.driver.execute_script("arguments[0].click();", show_more[0])
                    sleep(10)
                    show_more = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Show more')]")
            page_source = Selector(text=self.driver.page_source)
            url = self.driver.current_url
            restaurants = page_source.xpath("//a[contains(@href,'/store/')]")
            for rest in restaurants:
                try:
                    rest_name = rest.xpath('./h3/text()').get()
                    yield {
                        'postcode': postcode,
                        'url_postcode': url,
                        'total_rest_n': len(restaurants),
                        'restaurant name': rest_name,
                        'restaurant url': 'https://www.ubereats.com' + rest.xpath('./@href').get()
                    }
                except:
                    pass


