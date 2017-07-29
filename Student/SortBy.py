"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: June 19, 2017 @ 7:00pm
Author: Himadri Sharma
Place: Noida, India
Purpose: To automate Sort By functionality testing for "https://learn.spayee.com/store"
Browser : Chrome
"""

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
from selenium.common.exceptions import NoSuchElementException
from PathCreator import Path


path = Path.returnPath()


class SortBy(unittest.TestCase) :

    @classmethod
    def setUpClass(self):
        self.driver=webdriver.Chrome(path)
        self.driver.get("https://learn.spayee.com/store/eBooks/Current%20Affairs/2016")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_Books_selection(self):
        driver = self.driver
        try:
            elem=Select(self.driver.find_element_by_name("sortBy"))
            low_price = elem.select_by_index(3)
            books =  driver.find_elements_by_tag_name('strong')
            max_price = 0
            for book in books:
                cur_price = book.get_attribute('innerText')
                cur_price = int(cur_price[3:])
                if max_price <= cur_price:
                    max_price = cur_price
                else:
                    print('fail1')
                    break

            elem=Select(self.driver.find_element_by_name("sortBy"))
            high_price = elem.select_by_index(4)
            books =  driver.find_elements_by_tag_name('strong')
            max_price = books[0].get_attribute('innerText')
            max_price = int(max_price[3:])
            for book in books:
                cur_price = book.get_attribute('innerText')
                cur_price = int(cur_price[3:])
                if max_price >= cur_price:
                    max_price = cur_price
                else:
                    print('fail2')
                    break

            elem=Select(self.driver.find_element_by_name("sortBy"))
            title = elem.select_by_index(5)
            books =  driver.find_elements_by_class_name('bookDetails')
            first_string = "AAAA"
            for book in books:
                cur_string = book.find_element_by_tag_name('a').get_attribute('innerText')
                if first_string <= cur_string:
                    first_string = cur_string
                else:
                    print('fail3')
                    break    

        except NoSuchElementException:
            assert 0, "can't find input with such id"

    @classmethod
    def tearDownClass(self):
     self.driver.close()

if __name__ ==  "__main__":
    unittest.main()
