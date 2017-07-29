"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: June 11, 2017 @ 2:49pm
Author: Ankit Kumar Singh
Place: Noida, India
Purpose: To verify if password can be changed for "https://learn.spayee.com/changePassword" upon login.
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


class ChangePassword(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(path)
        self.email = "ankitsingh095@outlook.com"
        self.password = "spayee123"
        self.driver.get("https://learn.spayee.com/authenticate")
        self.driver.implicitly_wait(10)
        
    def test_new_password(self):
        driver = self.driver
        Login.login_authenticate(driver, self.email, self.password)
        driver.find_element_by_class_name('dropdown-toggle').click()
        time.sleep(1)
        driver.execute_script("""document.querySelector('[href="/myprofile"]').click()""")
        driver.execute_script("""document.querySelector('[href="/changePassword"]').click()""")
        driver.find_element_by_id("oldPassword").send_keys(self.password)
        driver.find_element_by_id("newPassword").send_keys(self.password)
        driver.find_element_by_id("confirmPassword").send_keys(self.password)
        driver.execute_script("""document.querySelector('[type="submit"]').click()""")
        time.sleep(2)
        driver.find_element_by_id("noty_topCenter_layout_container").is_displayed()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
