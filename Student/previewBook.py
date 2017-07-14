"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: July 11, 2017 @ 6:30pm
Author: Ankit Kumar Singh
Place: Noida, India
Purpose: To verify that locked pages are not accessible for "https://learn.spayee.com".
Browser : Chrome
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import unittest
import time

path = os.getcwd()
path = path + "/chromedriver"


class PreviewBookTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(path)
        self.driver.get("https://learn.spayee.com/store/eBooks/description/UPSC-IAS-Topicwise-Previous-Year-Papers-1997-2014-Gk-Publications-0f56afa9-c235-470f-9987-bf4fd1d7c080")
        self.driver.implicitly_wait(10)

    def test_previewBook(self):
        driver = self.driver
        assert 'Preview' in driver.page_source
        driver.find_elements_by_tag_name('strong')[0].click()
        slidemenu = driver.find_elements_by_class_name('slidemenu')[0]
        locked_pages = slidemenu.find_elements_by_class_name('icon-locked')
        Reading_frame = driver.find_element_by_id('pagingContainer')
        for page in locked_pages:
            page.click()
            driver.switch_to.frame(Reading_frame)
            assert 'TO READ MORE' in driver.page_source
            driver.switch_to.default_content()
            
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
