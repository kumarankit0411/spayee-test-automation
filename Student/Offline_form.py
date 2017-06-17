from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import os

path = os.getcwd()
path = path + '/chromedriver'

class Offline_Chat(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(path)
        self.driver.get("http://www.spayee.com")
        self.driver.implicitly_wait(10)

    def test_chat(self):
        driver = self.driver
        a = driver.find_elements_by_xpath('//*[@title="chat widget"]')
        driver.switch_to.frame(a[1])
        driver.find_element_by_id("maximizeChat").click()
        
    def tearDownClass(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()
