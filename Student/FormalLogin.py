"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: June 12, 2017 @ 5:15pm
Author: Ankit Kumar Singh
Place: Noida, India
Purpose: To verify login for "https://learn.spayee.com/store".
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import os
from PathCreator import Path


path = Path.returnPath()


class FormalLogin(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(path)
        self.email = "ankitsingh095@outlook.com"
        self.pwd = "spayee123"
        self.driver.get("http:///learn.spayee.com")
        self.driver.implicitly_wait(10)

    def test_login_formal(self):
        assert "UPSC" in self.driver.title
        driver = self.driver
        login_button = driver.find_element_by_class_name("loginBtn")
        login_button.click()
        time.sleep(1)
        login_form = driver.find_elements_by_class_name('loginForm')[1]
        login_form.find_element_by_name('email').send_keys(self.email)
        login_form.find_element_by_name('password').send_keys(self.pwd)
        login_form.find_elements_by_xpath('//*[@type="submit"]')[3].click()

    @classmethod
    def tearDownClass(self):
        #assert self.driver.get_log('browser')==[]
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
        
