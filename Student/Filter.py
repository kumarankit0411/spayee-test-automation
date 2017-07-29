"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: June 19, 2017 @ 7:00pm
Author: Himadri Sharma
Place: Noida, India
Purpose: To verify if the filter is working
Browser : Chrome
"""

import unittest
from selenium import webdriver
import time
import os
from PathCreator import Path


path = Path.returnPath()


class Filter(unittest.TestCase) :

    @classmethod
    def setUpClass(self):
        self.driver=webdriver.Chrome(path)
        self.driver.get("https://learn.spayee.com/store")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_language_selection(self):
        driver = self.driver
        driver.find_elements_by_class_name('category')[0].click()
        driver.execute_script("""document.querySelector('[data-value="en"]').click()""")
        time.sleep(2)
        driver.execute_script("""document.querySelector('[data-value="Alok Ranjan"]').click()""")
        time.sleep(2)
        books = driver.find_element_by_id('contentDataItems')
        all_books = books.find_elements_by_class_name('book')
        all_books[0].click()
        driver.switch_to.window(driver.window_handles[1])
        author = driver.find_element_by_xpath('//*[@itemprop="author"]').get_attribute('content')
        assert author == "Alok Ranjan"
        language = driver.find_element_by_xpath('//*[@itemprop="inLanguage"]').get_attribute('content')
        assert language == "en"

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ ==  "__main__":
    unittest.main()
            
