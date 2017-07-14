"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: June 12, 2017 @ 6:30pm
Author: Himadri Sharma
Place: Noida, India
Purpose: To automate android app link functionality testing for "https://learn.spayee.com/store"
Browser : Chrome
"""

import unittest
from selenium import webdriver
import os

path = os.getcwd()
path = path + "/chromedriver"


class Android_app_link_test(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(path)
        self.driver.get("https://learn.spayee.com/store")
        
    def test_android_link(self):
        driver = self.driver
        elem = driver.find_element_by_class_name("icon-android").click()
        driver.switch_to_window(driver.window_handles[1])
        assert "UPSC IAS SSC IBPS Bank Exams – Android Apps on Google Play" in driver.title
        
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ ==  "__main__":
    unittest.main()
