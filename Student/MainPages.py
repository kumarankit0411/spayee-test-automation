"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: June 15, 2017 @ 7:00pm
Author: Himadri Sharma
Place: Noida, India
Purpose: To automate AEP(assessment, ebooks, packages) functionality testing for "https://learn.spayee.com/store"
Browser : Chrome
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import os
import time

path=os.getcwd()
path = path + "/chromedriver"


class MainPages(unittest.TestCase) :

    @classmethod
    def setUpClass(self):
        self.driver=webdriver.Chrome(path)
        self.driver.get("https://learn.spayee.com/store")
        self.driver.implicitly_wait(10)

    def test_assessment(self):
        driver = self.driver

        assert "UPSC" in driver.title
        elem=driver.find_elements_by_class_name('dropdown-toggle')[0]
        hover=ActionChains(self.driver).move_to_element(elem)
        hover.perform() #only hovering and not clikcing

        elem=driver.find_element_by_partial_link_text("Assessments")
        hover=ActionChains(self.driver).move_to_element(elem)
        hover.perform()
        elem.send_keys(Keys.ENTER)
        self.assertEqual(driver.title, "Spayee Learn assessments")   

    def test_packages(self):
        driver = self.driver
        
        elem=driver.find_elements_by_class_name('dropdown-toggle')[0]
        hover=ActionChains(self.driver).move_to_element(elem)
        hover.perform()

        elem=driver.find_element_by_partial_link_text("Packages")
        hover=ActionChains(self.driver).move_to_element(elem)
        hover.perform()
        elem.send_keys(Keys.ENTER)
        self.assertEqual(driver.title, "Spayee Learn packages") 

    def test_ebooks(self):
        driver = self.driver
        
        elem=driver.find_elements_by_class_name('dropdown-toggle')[0]
        hover=ActionChains(self.driver).move_to_element(elem)
        hover.perform()

        elem=driver.find_element_by_partial_link_text("eBooks")
        hover=ActionChains(self.driver).move_to_element(elem)
        hover.perform()
        elem.send_keys(Keys.ENTER)
        self.assertEqual(driver.title, "Spayee Learn eBooks") 

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ ==  "__main__":
    unittest.main()
