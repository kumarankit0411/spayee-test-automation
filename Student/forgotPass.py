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


class ForgotPassword(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(path)
        self.email = "ankitsingh095@outlook.com"
        self.driver.get("http:///learn.spayee.com")
        self.driver.implicitly_wait(10)

    def test_forgot_password_fail(self):
        assert "UPSC" in self.driver.title
        driver = self.driver
        login_button = driver.find_element_by_class_name("loginBtn")
        login_button.click()
        time.sleep(1)
        driver.find_elements_by_class_name('forgotPassword')[1].click()
        time.sleep(1)
        assert driver.find_element_by_id('noty_topCenter_layout_container').is_displayed()

    def test_forgot_password_pass(self):
        driver = self.driver
        driver.find_elements_by_name('email')[3].send_keys(self.email)
        driver.find_elements_by_class_name('forgotPassword')[1].click()
        time.sleep(1)
        alert = driver.switch_to_alert()
        alert_text = alert.text
        self.assertEqual("Do you really want to reset your password?", alert_text)

    @classmethod
    def tearDownClass(self):
        #assert self.driver.get_log('browser')==[]
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
        
