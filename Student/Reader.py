"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: June 17, 2017 @ 6:11pm
Author: Ankit Kumar Singh
Place: Noida, India
Purpose: To test the book reader for "https://learn.spayee.com/store"
Test performed sequentially in order they are written
Browser : Chrome

Progress: open page and search verification
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import unittest

path = os.getcwd()
path = path + '/chromedriver'


class Read_book(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(path)
        self.driver.get("https://learn.spayee.com/store")
        self.driver.implicitly_wait(10)

    def test_reader(self):
        driver = self.driver
        btn = driver.find_elements_by_xpath('//*[text()="READ NOW"]/parent::a')
        btn[0].click()
        driver.switch_to.window(driver.window_handles[1])
        topics = driver.find_elements_by_xpath('//*[@class="slidemenu"]/div')
        assert len(topics)>0
        
        book = driver.find_element_by_class_name('book-title')
        title = book.get_attribute('innerHTML')
        title = title.split()
        
        driver.find_element_by_xpath('//*[@title="Search Book"]').click()
        driver.find_element_by_id('searchBookText').send_keys(title[0])
        driver.find_element_by_id('searchBookBtn').click()
        res = driver.find_elements_by_class_name('hi')
        for i in res:
            word = i.get_attribute('innerHTML').lower()
            assert word == title[0].lower()
            
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
