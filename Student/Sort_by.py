"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: June 19, 2017 @ 7:00pm
Author: Himadri Sharma
Place: Noida, India
Purpose: To automate Sort By functionality testing for "https://learn.spayee.com/store"
Browser : Chrome
"""

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os

path = os.getcwd()
path = path + "/chromedriver"


class SortBy_check(unittest.TestCase) :

    @classmethod
    def setUpClass(self):
        self.driver=webdriver.Chrome(path)
        self.driver.get("https://learn.spayee.com/store/eBooks/Current%20Affairs/2016")
        self.driver.maximize_window()

    def test_Books_selection(self):
        try:
            elem=Select(self.driver.find_element_by_class_name("redirectOnChange"))
            for i in range(0,6):
                (elem.select_by_index(i))
                print("test  successful")
        except NoSuchElementException:
            assert 0, "can't find input with such id"

    @classmethod
    def tearDownClass(self):
     self.driver.close()

if __name__ ==  "__main__":
    unittest.main()
