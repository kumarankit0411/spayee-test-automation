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
from PathCreator import Path


path = Path.returnPath()


class Enquiry(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(path)
        self.name = "Ankit Kumar Singh"
        self.email = "random_test@randommail.com"
        self.phone = "09876543233"
        self.query = "this is a test...please ignore"
        self.driver.get('http://learn.spayee.com/store')
        self.driver.implicitly_wait(10)

    def test_enquiry(self):
        driver = self.driver
        driver.find_element_by_id('enquiry-btn').click()
        time.sleep(2)
        enquiry_form = driver.find_element_by_xpath('//*[@action="/enquiry"]')
        enquiry_form.find_element_by_name('name').send_keys(self.name)
        enquiry_form.find_element_by_name('email').send_keys(self.email)
        enquiry_form.find_element_by_name('phone').send_keys(self.phone)
        enquiry_form.find_element_by_name('query').send_keys(self.query)
        driver.find_element_by_xpath('//button[text()="OK "]').click()
   
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
