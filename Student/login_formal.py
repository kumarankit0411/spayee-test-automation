from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import os

path = os.getcwd()
path = path + "/chromedriver"

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Chrome(path)
        inst.user = "ankitsingh095@outlook.com"
        inst.pwd = "spayee123"
        inst.driver.get("http:///learn.spayee.com")

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

    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
        
