"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: June 20, 2017 @ 05:05pm
Author: Ankit Kumar Singh
Place: Noida, India
Purpose: To verify if downlaod button asks for downloading apps for any given book
Browser : Chrome
"""

import unittest
from selenium import webdriver
import os
import time

path = os.getcwd()
path = path + "/chromedriver"


class DownloadBook(unittest.TestCase) :

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(path)
        self.driver.get("https://learn.spayee.com/store/eBooks/read/Modern-India-Synergy-IAS-Notes-Mohanti-Sir-cfc458a8-9db4-48aa-9dd1-1347996f3f42")
        self.driver.implicitly_wait(10)

    def test_downloadBook(self):
        driver = self.driver
        driver.find_element_by_id("bookDownloadBtn").click()
        android, apple = driver.find_elements_by_xpath('//*[@id="cboxContent"]//a')
        print(android, apple)
        assert android is not None
        assert apple is not None

    @classmethod
    def tearDownClass(self):
            self.driver.quit()

if __name__ ==  "__main__":
    unittest.main()
