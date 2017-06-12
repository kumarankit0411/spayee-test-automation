"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: June 12, 2017 @ 5:04pm
Author: Ankit Kumar Singh
Place: Noida, India
Purpose: To automate apple store link functionality testing for "https://learn.spayee.com/store"
Test performed sequentially in order they are written
Browser : Chrome
"""

import unittest
from selenium import webdriver
import os

path = os.getcwd()
path = path + "/chromedriver"


class Apple_app_link_test(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(path)
        self.driver.get("https://learn.spayee.com/store")
        
    def test_search_in_spayee(self):
        driver = self.driver
        driver.find_element_by_class_name("icon-apple").click()
        driver.switch_to_window(driver.window_handles[1])
        assert "Spayee Learn on the App Store" in driver.title

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ ==  "__main__":
    unittest.main()
