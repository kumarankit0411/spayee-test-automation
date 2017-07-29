"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: July 11, 2017 @ 5:20pm
Author: Ankit Kumar Singh
Place: Noida, India
Purpose: To test signup functionality for "https://learn.spayee.com/authenticate".
Browser : Chrome
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import unittest
import time
from PathCreator import Path


path = Path.returnPath()


class AuthSignUp(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(path)
        self.username = "ankitsingh095@outlook.com"
        self.password = "spayee123"
        self.name = "Ankit Kr. Singh"
        self.phone = "7310654986"
        self.driver.get("https://learn.spayee.com/authenticate")

    def test_signup(self):
        driver = self.driver
        driver.find_element_by_id('newUserBtn').click()
        driver.find_elements_by_name("email")[1].send_keys(self.username)
        driver.find_elements_by_name("password")[1].send_keys(self.password)
        driver.find_element_by_name("confirmPassword").send_keys(self.password)
        driver.find_element_by_name("fname").send_keys(self.name)
        driver.find_element_by_name("phone").send_keys(self.phone)
        driver.find_elements_by_xpath("//*[@class='form-actions']/button")[2].click()
        time.sleep(1)
        if driver.find_element_by_class_name('noty_text').is_displayed():
            pass
        else:
            assert "My Library" in driver.page_source

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
