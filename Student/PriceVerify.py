"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: June 13, 2017 @ 10:43pm
Author: Himadri Sharma & Ankit Kumar Singh
Place: Noida, India
Purpose: To verify the price of every book for "https://learn.spayee.com/store".
Browser : Chrome
"""

import unittest
from selenium import webdriver
import os
from selenium.webdriver import ActionChains
import re
import time
from PathCreator import Path


path = Path.returnPath()

class PriceVerify(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(path)
        self.driver.get("https://learn.spayee.com/store")
        self.driver.implicitly_wait(10)

    def test_ebooks_price(self):
        driver = self.driver
        elem = driver.find_element_by_partial_link_text("eBooks").click()
        #price verification
        viewAll = driver.find_element_by_xpath('//label[text()="Free eBooks"]//following-sibling::a')
        pos = viewAll.location_once_scrolled_into_view
        x_cord = pos['x']
        y_cord = pos['y']
        driver.execute_script('window.scrollTo({}, {});'.format(x_cord, y_cord-200))
        viewAll.click()
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
        check = """document.querySelector("[data-value='{}']").click()"""
        driver.execute_script(check.format('Under100'))
        driver.execute_script(check.format('Arihant'))
        driver.find_element_by_xpath('//select/option[@value="highprice"]').click()
        
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ ==  "__main__":
    unittest.main()
