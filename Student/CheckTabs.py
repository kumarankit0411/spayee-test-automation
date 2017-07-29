"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: June 13, 2017 @ 5:33pm
Author: Himadri Sharma & Ankit Kumar Singh
Place: Noida, India
Purpose: To check the ebook assessment and packages tab functionality for "https://learn.spayee.com/store".
Browser : Chrome
"""

import unittest
from selenium import webdriver
import os
import time

path = os.getcwd()
path = path + "/chromedriver"


class CheckTabs(unittest.TestCase) :

    @classmethod
    def setUpClass(self):
        self.driver=webdriver.Chrome(path)
        self.driver.get("https://learn.spayee.com/store")
        self.driver.implicitly_wait(10)

    def test_ebooks(self):
        driver = self.driver
        driver.execute_script("""document.querySelector('[href="#_page_1"]').click()""")
        time.sleep(1)
        '''counting the no. of category of books available under ebooks tab'''
        category_links = driver.execute_script("""return document.getElementById('_page_1').firstElementChild.childElementCount""")
        assert (category_links)>=16
        
    def test_assessment(self):
        driver = self.driver
        driver.execute_script("""document.querySelector('[href="#_page_2"]').click()""")
        time.sleep(2)
        '''counting the no. of category of books available under assessment tab'''
        category_links = driver.execute_script("""return document.getElementById('_page_2').firstElementChild.childElementCount""")
        assert (category_links)>=2
        
    def test_package(self):
        driver=self.driver
        driver.execute_script("""document.querySelector('[href="#_page_4"]').click()""")
        time.sleep(1)
        '''counting the no. of category of books available under packages tab'''
        category_links = driver.execute_script("""return document.getElementById('_page_4').firstElementChild.childElementCount""")
        assert (category_links)>=8

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ ==  "__main__":
    unittest.main()
