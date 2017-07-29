"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: July 10, 2017 @ 7:14pm
Author: Himadri Sharma
Place: Noida, India
Purpose: To verify profile of logged in user for "https://learn.spayee.com/"
Browser : Chrome
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import unittest
import time
from LoginPage import Login
    
path = os.getcwd()
path = path + "/chromedriver"


class Profile(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(path)
        self.email = "ankitsingh095@outlook.com"
        self.pwd = "spayee123"
        self.driver.get("https://learn.spayee.com")
        self.driver.implicitly_wait(10)
        
    def test_verify_profile(self):
        driver = self.driver
        Login.login(driver, self.email, self.pwd)
        driver.find_element_by_class_name('icon-cog').click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('My Profile').click()
        email = driver.find_element_by_id('email')
        assert email.get_attribute('value') == self.email
        name = driver.find_element_by_id('id_fname')
        assert name.get_attribute('value') == "Ankit Kr. Singh"
        phone = driver.find_element_by_id('id_phone')
        assert phone.get_attribute('value') == "7310654986"
        driver.execute_script('document.getElementById("id_fname").value = "Ankit Kr. Singh"')
        driver.find_element_by_xpath('//*[@type="submit"]').click()
        time.sleep(1)
        driver.find_element_by_id("noty_topCenter_layout_container").is_displayed()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
