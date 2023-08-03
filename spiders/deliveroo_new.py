import scrapy
from scrapy import Selector
import pandas as pd
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


class Deliveroo2Spider(scrapy.Spider):
    name = 'deliveroo2'
    allowed_domains = ['deliveroo.co.uk']
    start_urls = ['https://deliveroo.co.uk/']

    def __init__(self):
        chrome_service = Service(
            executable_path='C:\\Users\\yh459\\PycharmProjects\\UberEats(forJody)\\chromedriver.exe')
        self.driver = webdriver.Chrome(service=chrome_service)

    def parse(self, response):
        # postcodes = pd.read_excel('V:\\P8_PHI\\DPH\\Yuru Huang\\UberEats(forJody)\\IFPS 2023\\Postcodes to scrape 2023-03-02.xlsx')['Postcode units to scrape']
        # postcodes = ['TN278BT','AB101WE','B12JS','WA74XH','BH228PW','BD128PN','WA74XH']
        # postcodes = ['CB2 1DQ']
        i=0
        for postcode in postcodes:
            print(i)
            print(postcode)
            i+=1
            self.driver.get('https://deliveroo.co.uk/')
            sleep(5)
            # driver.find_element(By.XPATH,"//a[@class='ba bt bb bu c5 ah am bf bc ja dk b0 ax c6 c7 c8 bn bo']").click()
            input_element = self.driver.find_element(By.ID, "location-search")
            input_element.send_keys(postcode)
            sleep(1)
            input_element.send_keys(Keys.BACKSPACE)
            last_letter = postcode[-1]
            input_element.send_keys(last_letter)
            sleep(5)
            elements = self.driver.find_elements(By.XPATH, "//div[contains(@class,'ccl-c9fc3192a5030dce')]/ul/ul/li/button")
            if [] == elements:
                pass
            else:
                self.driver.execute_script("arguments[0].click();", elements[0])
                sleep(5)
                try:
                    self.driver.find_element(By.XPATH, "//h1[@id='modal-header-title']/span[contains(text(), 'not there yet')]")
                    start_url = 'not there yet'
                except:
                    start_url = self.driver.current_url
                    view_all = self.driver.find_elements(By.XPATH, "//button[@class='ccl-388f3fb1d79d6a36 ccl-9ed29b91bb2d9d02 ccl-59eced23a4d9e077 ccl-7be8185d0a980278']")
                    if [] == view_all:
                        pass
                    else:
                        self.driver.execute_script("arguments[0].click();", view_all[0])
                        sleep(8)
                    page_s = Selector(text=self.driver.page_source)
                    rest_urls = page_s.xpath('//a[contains(@href, "/menu/")]')
                    for rest_url in rest_urls:
                        yield {
                            'postcode': postcode,
                            'url_postcode': start_url,
                            'restaurant url': 'https://deliveroo.co.uk' + rest_url.xpath('./@href').get(),
                            'restaurant name': rest_url.xpath('./@aria-label').get()
                        }
