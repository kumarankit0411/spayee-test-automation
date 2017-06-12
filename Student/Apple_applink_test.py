import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

path = os.getcwd()
path = path + "/chromedriver"

class Apple_app_link_test(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Chrome(path)
        inst.driver.get("https://learn.spayee.com/store")
        
    def test_search_in_spayee(self):
        driver = self.driver
        elem = driver.find_element_by_class_name("icon-apple").click()
        driver.switch_to_window(driver.window_handles[1])
        assert "Spayee Learn on the App Store" in driver.title

    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()

if __name__ ==  "__main__":
    unittest.main()
