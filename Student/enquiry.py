"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: June 11, 2017 @ 3:20pm
Author: Ankit Kumar Singh
Place: Noida, India
Purpose: To automate 'enquiry' functionality testing for "https://learn.spayee.com/store".
"""

from selenium import webdriver
import unittest
import time
import os

path = os.getcwd()
path = path + "/chromedriver"


class Enquiry_test(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(path)
        self.name = "Ankit Kumar Singh"
        self.email = "random_test@randommail.com"
        self.phone = "09876543233"
        self.query = "this is a test...please ignore"
        self.driver.get('http://learn.spayee.com/store')

    def test_enquiry(self):
        driver = self.driver
        driver.find_element_by_id('enquiry-btn').click()
        time.sleep(2)
        elem = driver.find_element_by_xpath('//form[@class="padding20"]//input[@name="name"]')
        elem.send_keys(self.name)
        elem = driver.find_element_by_xpath('//form[@class="padding20"]//input[@name="email"]')
        elem.send_keys(self.email)
        elem = driver.find_element_by_xpath('//form[@class="padding20"]//input[@name="phone"]')
        elem.send_keys(self.phone)
        elem = driver.find_element_by_tag_name("textarea")
        elem.send_keys(self.query)
        elem = driver.find_element_by_xpath('//button[text()="OK "]')
        elem.click()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
