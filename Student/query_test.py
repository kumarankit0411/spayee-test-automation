"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: June 12, 2017 @ 11:34pm
Author: Himadri Sharma
Place: Noida, India
Purpose: To automate query box search functionality testing for "https://learn.spayee.com/store"
Test performed sequentially in order they are written
Browser : Chrome
"""

from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import os

path = os.getcwd()
path = path + "/chromedriver"


class Query_box_test(unittest.TestCase):

    @classmethod   
    def setUpClass(self):
        self.driver = webdriver.Chrome(path)
        self.driver.get("https://learn.spayee.com/store")
        self.driver.implicitly_wait(10)

    def test_search_query(self):
        driver = self.driver
        elem = driver.find_element_by_name('query')
        elem.send_keys("upsc books")
        elem.send_keys(Keys.ENTER)
        assert "Showing" in driver.page_source

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
