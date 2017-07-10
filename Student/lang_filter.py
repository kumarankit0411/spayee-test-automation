"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: June 19, 2017 @ 7:00pm
Author: Himadri Sharma
Place: Noida, India
Purpose: To automate Sort By  functionality testing for "https://learn.spayee.com/store"
Test performed sequentially in order they are written
Browser : Chrome
"""

import unittest
from selenium import webdriver
import time
import os

path = os.getcwd()
path = path + "/chromedriver"


class Language_check(unittest.TestCase) :

    @classmethod
    def setUp(self):
        self.driver=webdriver.Chrome(path)
        self.driver.get("https://learn.spayee.com/store/eBooks")
        self.driver.maximize_window()
        time.sleep(3)

    @classmethod
    def test_language_selection(self):

            elem=self.driver.find_element_by_xpath('//*[@id="langFilter"]/li/ul/li[1]/a/label')
            elem.click()
            time.sleep(3)
            elem.click()

            elem=self.driver.find_element_by_xpath('//*[@id="langFilter"]/li/ul/li[2]/a/label')
            elem.click()
            time.sleep(3)
            elem.click()

            elem=self.driver.find_element_by_xpath('//*[@id="langFilter"]/li/ul/li[3]/a/label')
            elem.click()
            time.sleep(3)

    @classmethod
    def tearDown(self):
     self.driver.close()

if __name__ ==  "__main__":
    try:
        unittest.main()
    except:
        print("some error")        
