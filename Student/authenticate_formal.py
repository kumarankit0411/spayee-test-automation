"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: June 10, 2017 @ 1:53am
Author: Ankit Kumar Singh
Place: Noida, India
Purpose: To automate login and logout functionality testing for "https://learn.spayee.com/authenticate".
Test performed sequentially in order they are written
Browser : Chrome
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import unittest
import time

path = os.getcwd()
path = path + "/chromedriver"


class AuthenticateTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(path)
        self.username = "ankitsingh095@outlook.com"
        self.password = "spayee123"
        self.driver.get("https://learn.spayee.com/authenticate")

    def test_login(self):
        driver = self.driver
        elem = driver.find_element_by_name("email")
        elem.send_keys(self.username)
        elem = driver.find_element_by_name("password")
        elem.send_keys(self.password)
        elem.send_keys(Keys.RETURN)

    def test_logout(self):
        driver = self.driver
        driver.find_element_by_xpath('//a[@class="dropdown-toggle"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//ul[@class="dropdown-menu inverse place-right"]//li//a[text()="Log Out"]').click()
        
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
