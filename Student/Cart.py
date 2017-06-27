"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: June 19, 2017 @ 6:59pm
Author: Ankit Kumar Singh
Place: Noida, India
Purpose: To check add to cart functionality testing for "https://learn.spayee.com/store".
Browser : Chrome
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import os
import time

path = os.getcwd()
path = path + '/chromedriver'


class Cart(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(path)
        self.driver.get('https://learn.spayee.com/store')
        self.driver.implicitly_wait(10)
        self.user = "ankitsingh095@outlook.com"
        self.pwd = "spayee123"
    
    def login(self):
        driver = self.driver
        assert "UPSC" in driver.title
        login_button = driver.find_element_by_class_name("loginBtn")
        login_button.click()
        time.sleep(1)
        elem = driver.find_element_by_xpath('//*[@id="cboxLoadedContent"]//form[@class="loginForm nbm"]//input[@name="email"]')
        elem.send_keys(self.user)
        elem = driver.find_element_by_xpath('//*[@id="cboxLoadedContent"]//form[@class="loginForm nbm"]//input[@name="password"]')
        elem.send_keys(self.pwd)
        elem.send_keys(Keys.RETURN)
    
    def test_addToCart(self):
        self.login()
        driver = self.driver
        books = driver.find_elements_by_xpath('//*[@class="buyBtn has-spinner"]')
        books[0].click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="cboxContent"]//button[text()="Continue"]').click()
        time.sleep(1)
        books[1].click()
        time.sleep(1)
        book_count = driver.find_elements_by_xpath('//*[@id="cboxContent"]//tbody/tr')
        assert len(book_count)>1
        assert driver.find_element_by_id('colorbox').is_displayed()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
