"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: June 19, 2017 @ 6:59pm
Author: Ankit Kumar Singh
Place: Noida, India
Purpose: To verify addition and deletion of item from the cart for "https://learn.spayee.com/store".
Browser : Chrome
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import os
import time
from LoginPage import Login
from PathCreator import Path


path = Path.returnPath()


class Cart(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(path)
        self.driver.get('https://learn.spayee.com/store')
        self.driver.implicitly_wait(10)
        self.user = "ankitsingh095@outlook.com"
        self.pwd = "spayee123"
        self.book_count = 0
    
    def test_addToCart(self):
        driver = self.driver
        Login.login(driver, self.user, self.pwd)
        books = driver.find_elements_by_class_name('buyBtn')
        books[0].click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="cboxContent"]//button[text()="Continue"]').click()
        time.sleep(1)
        books[1].click()
        time.sleep(1)
        self.book_count = len(driver.find_elements_by_xpath('//*[@id="cboxContent"]//tbody/tr'))
        assert self.book_count>=2

    def test_removeFromCart(self):
        driver = self.driver
        book_count_before_removal = len(driver.find_elements_by_xpath('//*[@id="cboxContent"]//tbody/tr'))
        driver.find_elements_by_class_name('removeItemBtn')[0].click()
        time.sleep(1)
        book_count_after_removal = len(driver.find_elements_by_xpath('//*[@id="cboxContent"]//tbody/tr'))
        assert (book_count_after_removal + 1) == book_count_before_removal
        
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
