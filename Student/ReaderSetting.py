"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: July 12, 2017 @ 9:00pm
Author: Himadri Sharma
Place: Noida, India
Purpose: To automate readers setting functionality testing for "https://learn.spayee.com/store"
Browser : Chrome
"""


import unittest
from selenium import webdriver
import time
import os
from PathCreator import Path


path = Path.returnPath()


class ReaderSetting(unittest.TestCase) :

    @classmethod
    def setUpClass(self):
        self.driver=webdriver.Chrome(path)
        self.driver.get("https://learn.spayee.com/store/eBooks/read/Economic-Survey--Volume-I-d67a30cc-4519-46fa-b7de-061dda914676")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_readers_fonts(self):
        self.driver.find_element_by_xpath('//*[@id="fontSizeChange"]/button[1]/i').click()
        style = self.driver.execute_script('return document.getElementById("pagingContainer").contentDocument.body.getAttribute("style")')
        font_size = style[style.index('px')-2:style.index('px')]
        assert float(font_size)==16

        self.driver.find_element_by_xpath('//*[@id="fontSizeChange"]/button[2]/i').click()
        style = self.driver.execute_script('return document.getElementById("pagingContainer").contentDocument.body.getAttribute("style")')
        font_size = style[style.index('px')-2:style.index('px')]
        assert float(font_size)==18

    def test_line_height(self):
        self.driver.find_element_by_xpath('//*[@id="readerSettingsBtn"]').click()
        time.sleep(3)

        '''small line height'''
        self.driver.find_element_by_xpath('//*[@id="lineHeightChange"]/button[1]').click()
        style = self.driver.execute_script('return document.getElementById("pagingContainer").contentDocument.body.getAttribute("style")')
        line_height = style[style.index('.')-1:style.index('.')+2]
        assert float(line_height)==1.5 

        '''medium line height'''
        self.driver.find_element_by_xpath('//*[@id="lineHeightChange"]/button[2]').click()
        style = self.driver.execute_script('return document.getElementById("pagingContainer").contentDocument.body.getAttribute("style")')
        line_height = style[style.index('.')-1:style.index('.')+2]
        assert float(line_height)==2.5

        '''large line height'''
        self.driver.find_element_by_xpath('//*[@id="lineHeightChange"]/button[3]').click()
        style = self.driver.execute_script('return document.getElementById("pagingContainer").contentDocument.body.getAttribute("style")')
        line_height = style[style.index('.')-1:style.index('.')+2]
        assert float(line_height)==3.5

    def test_readers_justify(self):
        '''Center alignment'''
        self.driver.find_element_by_class_name("icon-paragraph-center").click()
        class_name = self.driver.execute_script('return document.getElementById("pagingContainer").contentDocument.body.getAttribute("class")')
        assert class_name=="spee-txt-align-center"

        '''Justify alignment'''
        self.driver.find_element_by_class_name("icon-paragraph-justify").click()
        class_name = self.driver.execute_script('return document.getElementById("pagingContainer").contentDocument.body.getAttribute("class")')
        assert class_name=="spee-txt-align-justify"

        '''Left alignment'''
        self.driver.find_element_by_class_name("icon-paragraph-left").click()
        class_name = self.driver.execute_script('return document.getElementById("pagingContainer").contentDocument.body.getAttribute("class")')
        assert class_name=="spee-txt-align-left"   

    def test_readers_theme(self):
        '''Normal mode'''
        self.driver.find_element_by_class_name('icon-sun').click
        class_name = self.driver.execute_script('return document.getElementById("pagingContainer").contentDocument.body.getAttribute("class")')
        assert class_name=="spee-txt-align-left"

        '''Sepia mode'''
        elem=self.driver.find_element_by_class_name("icon-sun-2").click()
        class_name = self.driver.execute_script('return document.getElementById("pagingContainer").contentDocument.body.getAttribute("class")')
        assert class_name=="spee-txt-align-left sepia"

        '''Night mode'''
        elem=self.driver.find_element_by_class_name("icon-moon-2").click()
        class_name = self.driver.execute_script('return document.getElementById("pagingContainer").contentDocument.body.getAttribute("class")')
        assert class_name=="spee-txt-align-left night"

    def test_search_query(self):
        driver = self.driver
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

if __name__ ==  "__main__":
    unittest.main()
