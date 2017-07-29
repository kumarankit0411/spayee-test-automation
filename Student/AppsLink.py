"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: June 12, 2017 @ 5:04pm
Author: Ankit Kumar Singh
Place: Noida, India
Purpose: To automate apple store link functionality testing for "https://learn.spayee.com/store"
Test performed sequentially in order they are written
Browser : Chrome
"""

import unittest
from selenium import webdriver
import os
import time


path = os.getcwd()
path = path + "/chromedriver"


class AppsLink(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(path)
        self.driver.get("https://learn.spayee.com/store")
        self.driver.implicitly_wait(10)
        
    def test_1_apple_link(self):
        driver = self.driver
        driver.find_element_by_class_name("icon-apple").click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        self.assertEqual("Spayee Learn on the App Store", driver.title)
        driver.execute_script('window.close()')
        driver.switch_to.window(driver.window_handles[-1])

    def test_2_android_link(self):
        driver = self.driver
        elem = driver.find_element_by_class_name("icon-android").click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[-1])
        self.assertEqual("UPSC IAS SSC IBPS Bank Exams – Android Apps on Google Play", driver.title)
        driver.switch_to.window(driver.window_handles[-1])    

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ ==  "__main__":
    unittest.main()
