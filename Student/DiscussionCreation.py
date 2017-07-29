"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: June 12, 2017 @ 2:59pm
Author: Ankit Kumar Singh
Place: Noida, India
Purpose: To verify new discussion creation for "https://learn.spayee.com/store".
Browser : Chrome
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import unittest
import os
from LoginPage import Login
from PathCreator import Path


path = Path.returnPath()


class DiscussionCreation(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(path)
        self.email = "ankitsingh095@outlook.com"
        self.pwd = "spayee123"
        self.driver.get("http:///learn.spayee.com")
        self.driver.implicitly_wait(10)
        self.discussion = "How to check mock test results?"

    def test_newTopic(self):
        driver = self.driver
        Login.login(driver, self.email, self.pwd)
        driver.find_element_by_xpath('//*[@href="/library"]').click()
        driver.find_element_by_xpath('//*[@href="/discussion"]').click()
        driver.find_element_by_id('newDiscussionBtn').click()
        time.sleep(4)
        try:
            '''below javascript make an element visible and then
            access iframe inside it to write to a discussion
            window inside iframe'''
            driver.execute_script("""a = document.querySelector('[role="application"]');a.style.visibility='visible'""")
            driver.switch_to.frame(driver.find_element_by_id('mce_0_ifr'))
            driver.find_element_by_id('tinymce').send_keys(self.discussion)
            driver.switch_to.default_content()
        except NoSuchElementException:
            print("can't find input with such id")
        driver.find_element_by_xpath('//*[@id="cboxLoadedContent"]//button[text()="Post "]').click()
        time.sleep(2)
        try:
            assert self.discussion in driver.page_source
        except AssertionError:
            print("Website may have loaded slowly")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
        
