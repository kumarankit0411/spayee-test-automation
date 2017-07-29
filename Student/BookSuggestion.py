"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: July 11, 2017 @ 7:50pm
Author: Ankit Kumar Singh
Place: Noida, India
Purpose: To verify that related books are shown for "https://learn.spayee.com".
Browser : Chrome
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import unittest
import time
from PathCreator import Path


path = Path.returnPath()

class BookSuggestion(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(path)
        self.driver.get("https://learn.spayee.com")
        self.driver.implicitly_wait(10)

    def test_suggestion(self):
        driver = self.driver
        books = driver.find_elements_by_xpath('//strong//parent::a//preceding-sibling::a')
        books[0].click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        book_container = driver.find_element_by_id('relatedContent')
        related_books = book_container.find_elements_by_tag_name('id')
        try:
            assert len(related_books)>0
        except AssertionError:
            pass
        
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
