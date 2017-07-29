"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: July 13, 2017 @ 3:00pm
Author: Himadri Sharma
Place: Noida, India
Purpose: To hide left and right pane in reader for "https://learn.spayee.com/store"
Browser : Chrome
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os

path = os.getcwd()
path = path + "/chromedriver"


class LeftClick(unittest.TestCase) :

    @classmethod
    def setUpClass(self):
        self.driver=webdriver.Chrome(path)
        self.driver.get("https://learn.spayee.com/store/eBooks/read/Economic-Survey--Volume-I-d67a30cc-4519-46fa-b7de-061dda914676")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_left_click(self):
        driver = self.driver
        try:
            '''To check if left pane is hiding'''
            driver.find_element_by_class_name('button-open-left').click()
            time.sleep(1)
            left_side_pane = driver.execute_script('return document.getElementsByClassName("reader-lhs")[0].getAttribute("style")')
            assert 'none' in left_side_pane

            '''To check if right pane is hiding'''
            driver.find_element_by_class_name('button-open-right').click()
            time.sleep(1)
            right_side_pane = driver.execute_script('return document.getElementsByClassName("reader-rhs")[0].getAttribute("style")')
            assert 'none' in right_side_pane
        except (NoSuchElementException, AssertionError):
            print('either element not found or assert gone wrong')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ ==  "__main__":
    unittest.main()
