"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: June 20, 2017 @ 7:00pm
Author: Himadri Sharma
Place: Noida, India
Purpose: To automate readers setting functionality testing for "https://learn.spayee.com/store"
Test performed sequentially in order they are written
Browser : Chrome
"""


import unittest
from selenium import webdriver
import time
import os

path=os.getcwd()
path = path + "/chromedriver"


class ReadersSetting_check(unittest.TestCase) :

    @classmethod
    def setUpClass(self):
        self.driver=webdriver.Chrome(path)
        self.driver.get("https://learn.spayee.com/store/eBooks/read/Economic-Survey--Volume-I-d67a30cc-4519-46fa-b7de-061dda914676")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_readers_fonts(self):
        elem=self.driver.find_element_by_id("readerSettingsBtn")
        elem.click()
        elem=self.driver.find_element_by_xpath('//*[@id="fontSizeChange"]/button[1]/i')
        elem.click()
        time.sleep(3)
        elem=self.driver.find_element_by_xpath('//*[@id="fontSizeChange"]/button[2]/i')
        elem.click()
        time.sleep(3)
        print("test1 done")

    def test_line_height(self):
        elem=self.driver.find_element_by_xpath('//*[@id="readerSettingsBtn"]')
        elem.click()
        elem=self.driver.find_element_by_xpath('//*[@id="lineHeightChange"]/button[1]')
        elem.click()
        time.sleep(3)
        elem=self.driver.find_element_by_xpath('//*[@id="lineHeightChange"]/button[2]')
        elem.click()
        time.sleep(3)
        elem=self.driver.find_element_by_xpath('//*[@id="lineHeightChange"]/button[3]')
        elem.click()
        time.sleep(3)
        print("test2 done")

    def test_readers_justify(self):
        elem=self.driver.find_element_by_xpath('//*[@id="readerSettingsBtn"]')
        elem.click()
        elem=self.driver.find_element_by_class_name("icon-paragraph-left")
        elem.click()
        time.sleep(3)
        elem=self.driver.find_element_by_class_name("icon-paragraph-center")
        elem.click()
        time.sleep(3)
        elem=self.driver.find_element_by_class_name('icon-paragraph-justify')
        elem.click()
        time.sleep(3)
        print("test3 done")

    def test_annotations(self):
        elem=self.driver.find_element_by_xpath('//*[@id="readerSettingsBtn"]')
        elem.click()
        elem=self.driver.find_element_by_xpath('//*[@id="annoMode"]/button[1]')
        elem.click()
        time.sleep(3)
        elem=self.driver.find_element_by_xpath('//*[@id="annoMode"]/button[2]')
        elem.click()
        time.sleep(3)
        print("test4 done")

    def test_readers_theme(self):
        elem=self.driver.find_element_by_xpath('//*[@id="readerSettingsBtn"]')
        elem.click()
        elem=self.driver.find_element_by_class_name('icon-sun')
        elem.click()
        time.sleep(3)
        elem=self.driver.find_element_by_class_name("icon-sun-2")
        elem.click()
        time.sleep(3)
        elem=self.driver.find_element_by_class_name("icon-moon-2")
        elem.click()
        time.sleep(3)
        print("test5 done")

    @classmethod
    def tearDownClas(self):
     self.driver.close()

if __name__ ==  "__main__":
    unittest.main()
