"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: June 12, 2017 @ 2:59pm
Author: Ankit Kumar Singh
Place: Noida, India
Purpose: To automate new discussioon creation functionality testing for "https://learn.spayee.com/store".
Browser : Chrome
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import os

path = os.getcwd()
path = path + "/chromedriver"


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(path)
        self.user = "ankitsingh095@outlook.com"
        self.pwd = "spayee123"
        self.driver.get("http:///learn.spayee.com")
        self.driver.implicitly_wait(2)
        self.discussion = "How to check mock test results?"

    def test_login_formal(self):
        assert "UPSC" in self.driver.title
        driver = self.driver
        login_button = driver.find_element_by_class_name("loginBtn")
        login_button.click()
        time.sleep(1)
        elem = driver.find_element_by_xpath('//*[@id="cboxLoadedContent"]//form[@class="loginForm nbm"]//input[@name="email"]')
        elem.send_keys(self.user)
        elem = driver.find_element_by_xpath('//*[@id="cboxLoadedContent"]//form[@class="loginForm nbm"]//input[@name="password"]')
        elem.send_keys(self.pwd)
        elem.send_keys(Keys.RETURN)

    def test_newTopic(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@href="/library"]').click()
        driver.find_element_by_xpath('//*[@href="/discussion"]').click()
        time.sleep(2)
        driver.find_element_by_id('newDiscussionBtn').click()
        time.sleep(4)
        try:
            '''below javascript make an element visible and then
            access iframe inside it to write to a discussion
            window inside iframe'''
            driver.execute_script("a = document.getElementById('mceu_5');a.style.visibility='visible'")
            driver.switch_to.frame(driver.find_element_by_id('mce_0_ifr'))
            driver.find_element_by_id('tinymce').send_keys(self.discussion)
            driver.switch_to.default_content()
        except NoSuchElementException:
            assert 0, "can't find input with such id"
        driver.find_element_by_xpath('//*[@id="cboxLoadedContent"]//button[text()="Post "]').click()
        time.sleep(2)
        assert self.discussion in driver.page_source               

    @classmethod
    def tearDownClass(self):
        #console shows error or thumbnail missing always
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
        
