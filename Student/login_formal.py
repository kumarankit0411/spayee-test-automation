"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: June 12, 2017 @ 5:15pm
Author: Ankit Kumar Singh
Place: Noida, India
Purpose: To automate formal login functionality testing for "https://learn.spayee.com/store".
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import os

path = os.getcwd()
path = path + "/chromedriver"


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(path)
        self.user = "ankitsingh095@outlook.com"
        self.pwd = "spayee123"
        self.driver.get("http:///learn.spayee.com")

    def test_login_formal(self):
        assert "UPSC" in self.driver.title
        driver = self.driver
        login_button = driver.find_element_by_class_name("loginBtn")
        login_button.click()
        time.sleep(1)
        elem = driver.find_element_by_xpath('//*[@id="cboxLoadedContent"]//form[@class="loginForm nbm"]//input[@name="email"]')
        elem.send_keys(self.user)
        elem = driver.find_element_by_xpath('//*[@id="cboxLoadedContent"]//form[@class="loginForm nbm"]//input[@name="password"]')
        elem.send_keys(self.pwd)
        elem.send_keys(Keys.RETURN)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
        
