"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: July 10, 2017 @ 5:15pm
Author: Ankit Kumar Singh
Place: Noida, India
Purpose: To automate formal signup functionality testing for "https://teststore.spayee.com/store".
"""

from selenium import webdriver
import time
import unittest
import os
from PathCreator import Path


path = Path.returnPath()


class FormalSignUp(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(path)
        self.user = "sample@sample.com"
        self.pwd = "spayee123"
        self.name = "sample"
        self.phone = "1234567890"
        self.driver.get("http:///teststore.spayee.in")
        self.driver.implicitly_wait(10)

    def test_signup_formal(self):
        assert "UPSC" in self.driver.title
        driver = self.driver
        login_button = driver.find_element_by_class_name("loginBtn")
        login_button.click()
        time.sleep(1)
        driver.find_elements_by_class_name('icon-user-2')[1].click()
        driver.find_elements_by_name('email')[2].send_keys(self.user)
        driver.find_elements_by_name('password')[2].send_keys(self.pwd)
        driver.find_elements_by_name('confirmPassword')[1].send_keys(self.pwd)
        driver.find_elements_by_name('fname')[1].send_keys(self.name)
        driver.find_elements_by_name('phone')[1].send_keys(self.phone)
        driver.find_elements_by_xpath('//*[@class="form-actions"]/button')[4].click()
        time.sleep(1)
        if driver.find_element_by_class_name('noty_text').is_displayed():
            pass
        else:
            assert "My Library" in driver.page_source

    @classmethod
    def tearDownClass(self):
        #assert self.driver.get_log('browser')==[]
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
        
