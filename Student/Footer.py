"""
This script is written as a part of summer intern project 2017-18 for Spayee.
Date: July 12, 2017 @ 7:15pm
Author: Himadri Sharma
Place: Noida, India
Purpose: To verify if footer links are all working for "https://learn.spayee.com/store".
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import os
from PathCreator import Path


path = Path.returnPath()


class Footer(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(path)
        self.user = "ankitsingh095@outlook.com"
        self.pwd = "spayee123"
        self.driver.get("http:///learn.spayee.com")
        assert "UPSC" in self.driver.title

    def test_footer_faq_link(self):
        footer = self.driver.find_elements_by_xpath('//footer//a')
        footer[0].click()
        time.sleep(1)
        assert "Frequently Asked Questions" in self.driver.page_source

    def test_footer_aboutUs_link(self):
        footer = self.driver.find_elements_by_xpath('//footer//a')
        footer[1].click()
        time.sleep(1)
        assert "developed after years of research" in self.driver.page_source

    def test_footer_contactUs_link(self):
        footer = self.driver.find_elements_by_xpath('//footer//a')
        footer[2].click()
        time.sleep(1)
        assert "OFFICE:" in self.driver.page_source

    def test_footer_termsOfUse_link(self):
        footer = self.driver.find_elements_by_xpath('//footer//a')
        footer[3].click()
        time.sleep(1)
        assert "Your password is unique and exclusive to you" in self.driver.page_source

    def test_footer_privacyPolicy_link(self):
        footer = self.driver.find_elements_by_xpath('//footer//a')
        footer[4].click()
        time.sleep(1)
        assert "you can browse the Website without telling us" in self.driver.page_source

    def test_footer_refundPolicy_link(self):
        footer = self.driver.find_elements_by_xpath('//footer//a')
        footer[5].click()
        time.sleep(1)
        assert "Non-tangible irrevocable goods" in self.driver.page_source

    '''
    Commented because linkedIn wanted to sign in
    def test_footer_linkedIn_link(self):
        footer = self.driver.find_elements_by_xpath('//footer//a')
        footer[6].click()
        self.driver.switch_to.window(self.driver.window_handles[3])
        assert "A Times Internet portfolio company." in self.driver.page_source
        self.driver.switch_to.window(self.driver.window_handles[0])
    '''
    
    def test_footer_googlePlus_link(self):
        footer = self.driver.find_elements_by_xpath('//footer//a')
        footer[7].click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert "Spayee's posts" in self.driver.page_source
        self.driver.switch_to.window(self.driver.window_handles[0])

    '''
    Commented bcoz facebook asked for captcha verification
    Conclusion: Big players don't want bots to run on their website!!

    def test_footer_facebook_link(self):
        footer = self.driver.find_elements_by_xpath('//footer//a')
        footer[8].click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert "Education website" in self.driver.page_source
        self.driver.switch_to.window(self.driver.window_handles[0])
    '''
    
    def test_footer_twitter_link(self):
        footer = self.driver.find_elements_by_xpath('//footer//a')
        footer[9].click()
        self.driver.switch_to.window(self.driver.window_handles[2])
        assert "Competition In Focus" in self.driver.page_source
        self.driver.switch_to.window(self.driver.window_handles[0])
        
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
        
