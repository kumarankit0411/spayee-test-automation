"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: June 15, 2017 @ 7:00pm
Author: Himadri Sharma
Place: Noida, India
Purpose: To automate AEP(assessment, ebooks, packages) functionality testing for "https://learn.spayee.com/store"
Test performed sequentially in order they are written
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


class Dropdown_check(unittest.TestCase) :

    @classmethod
    def setUpClass(self):
        self.driver=webdriver.Chrome(path)
        self.driver.get("https://learn.spayee.com/store")

    @classmethod
    def test_dropdown(self):

        try:

            elem=self.driver.find_element_by_partial_link_text("eBooks")
            hover=ActionChains(self.driver).move_to_element(elem)
            hover.perform()

            time.sleep(4)

            print("part 1 success")

            elem=self.driver.find_element_by_partial_link_text("Assessments")
            hover=ActionChains(self.driver).move_to_element(elem)
            hover.perform()
            elem.send_keys(Keys.ENTER)
            time.sleep(2)

            print("part2 success")
            elem=self.driver.find_element_by_partial_link_text("Assessments")
            hover=ActionChains(self.driver).move_to_element(elem)
            hover.perform()

            elem=self.driver.find_element_by_partial_link_text("Packages")
            hover=ActionChains(self.driver).move_to_element(elem)
            hover.perform()
            elem.send_keys(Keys.ENTER)
            time.sleep(2)


            print("part3 success")


        except NoSuchElementException:
            assert 0, "can't find input with such id"

    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ ==  "__main__":
    unittest.main()
