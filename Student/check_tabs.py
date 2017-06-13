"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: June 13, 2017 @ 5:33pm
Author: Himadri Sharma & Ankit Kumar Singh
Place: Noida, India
Purpose: To check the ebook assessment and packages tab functionality for "https://learn.spayee.com/store".
Tests are performed in the sequenve they are written
Browser : Chrome
"""

import unittest
from selenium import webdriver
import os

path = os.getcwd()
path = path + "/chromedriver"


class Assement_package(unittest.TestCase) :

    @classmethod
    def setUpClass(self):
        self.driver=webdriver.Chrome(path)
        self.driver.get("https://learn.spayee.com/store")
        self.driver.implicitly_wait(2)

    def test_ebooks(self):
        driver = self.driver
        elem = driver.find_element_by_partial_link_text("EBOOKS").click()
        #counting the number of category of books available under ebooks tab
        category_links = driver.find_elements_by_xpath('//*[@id="_page_1"]//a[@class="button category"]')
        assert len(category_links)>=16
        
    def test_assessment(self):
        driver = self.driver
        driver.find_element_by_partial_link_text("ASSESSMENTS").click()
        #counting the number of category of books available under assessment tab
        category_links = driver.find_elements_by_xpath('//*[@id="_page_2"]//a[@class="button category"]')
        assert len(category_links)>=2
        
    def test_package(self):
        driver=self.driver
        elem=driver.find_element_by_partial_link_text("PACKAGES").click()
        #counting the number of category of books available under packages tab
        category_links = driver.find_elements_by_xpath('//*[@id="_page_4"]//a[@class="button category"]')
        assert len(category_links)>=8

    @classmethod
    def tearDownClass(self):
            self.driver.quit()

if __name__ ==  "__main__":
    unittest.main()
