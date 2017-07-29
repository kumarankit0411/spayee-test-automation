"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: June 14, 2017 @ 7:25pm
Author: Ankit Kumar Singh
Place: Noida, India
Purpose: To automate mock test functionality testing for "https://learn.spayee.com/store"
Browser : Chrome
"""

from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
import time
import unittest
from LoginPage import Login

path = os.getcwd()
path = path + '/chromedriver'


class MockTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(path)
        self.driver.get("https://learn.spayee.com/store")
        self.email = "ankitsingh095@outlook.com"
        self.pwd = "spayee123"
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_report_generator(self):
        driver = self.driver
        Login.login(driver, self.email, self.pwd)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@href="#_page_2"]').click()
        driver.find_elements_by_xpath('//*[text()="TAKE TEST"]')[0].click()
        time.sleep(4)
        driver.find_elements_by_class_name('text-muted')[1].click()
        driver.find_element_by_xpath('//*[@id="cboxContent"]//button[text()="Start"]').click()
        time.sleep(2)
        for i in range(1, 101):
            driver.execute_script("a = document.getElementsByClassName('list-content'); a[{}].click()".format(4*i-1))   #clicking the answer option D
            driver.find_element_by_id('saveNextBtn').click()
        driver.execute_script('document.getElementById("submitBtn").click()') 
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="cboxContent"]//button[text()="Submit "]').click()
        time.sleep(1)
        assert "Your Last Attempt" in driver.page_source    #report page contains this phrase

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
