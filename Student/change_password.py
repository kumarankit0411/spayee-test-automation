"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: June 11, 2017 @ 2:49pm
Author: Ankit Kumar Singh
Place: Noida, India
Purpose: To automate 'change password' functionality testing for "https://learn.spayee.com/changePassword" upon login.
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
        
    def test_new_password(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@class="icon-cog"]//parent::a').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@class="divider"]//following::a[text()="My Profile"]').click()
        driver.find_element_by_xpath('//a[text()=" Change Password"]').click()
        driver.find_element_by_id("oldPassword").send_keys(self.password)
        driver.find_element_by_id("newPassword").send_keys(self.password)
        driver.find_element_by_id("confirmPassword").send_keys(self.password)
        driver.find_element_by_xpath('//button[text()="Submit "]').click()
        time.sleep(2)
        driver.find_element_by_id("noty_topCenter_layout_container").is_displayed()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
