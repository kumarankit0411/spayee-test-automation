"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: June 13, 2017 @ 10:43pm
Author: Himadri Sharma & Ankit Kumar Singh
Place: Noida, India
Purpose: To verify the price of every book for "https://learn.spayee.com/store".
Tests are performed in the sequenve they are written
Browser : Firefox(will not work with chrome as of now due to unclickability of checkboxes)
"""

import unittest
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import re
import time

path = os.getcwd()
path = path + "/geckodriver"
print(path)

class Price_verify(unittest.TestCase) :

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox(executable_path=path)
        self.driver.get("https://learn.spayee.com/store")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_ebooks(self):
        driver = self.driver
        elem = driver.find_element_by_partial_link_text("eBooks").click()
        #price verification
        driver.find_element_by_xpath('//label[text()="Free eBooks"]//following-sibling::a').click()
        self.verify_price()
    
    def verify_price(self):
        driver = self.driver
        self.find_elements()
        self.temp = 0
        while True:
            elem = driver.find_elements_by_xpath('//i[@class="icon-cart on-left"]//following::strong')
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            if len(elem) == self.temp:
                break
            self.temp = len(elem)
            
        for each in elem:
            price = each.get_attribute('innerHTML')
            price = re.findall(r'\d+', price)[0]
            price = int(price)
            assert price<=100
                
    def find_elements(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@data-value="en"]').click()
        elem = driver.find_element_by_xpath('//*[@id="authorFilter"]//*[text()="Arihant "]//parent::a//child::span')
        elem.click()
        elem = driver.find_element_by_xpath('//*[@id="priceFilter"]//*[text()="Under 100 "]//parent::a//child::span')
        elem.click()
        driver.find_element_by_xpath('//select/option[@value="highprice"]').click()
        
    @classmethod
    def tearDownClass(self):
            self.driver.quit()

if __name__ ==  "__main__":
    unittest.main()
