from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Login():
    def __init__(self):
        pass

    def login(driver, username, password):
        assert "UPSC" in driver.title
        login_button = driver.find_element_by_class_name("loginBtn")
        login_button.click()
        time.sleep(1)
        elem = driver.find_element_by_xpath('//*[@id="cboxLoadedContent"]//form[@class="loginForm nbm"]//input[@name="email"]')
        elem.send_keys(username)
        elem = driver.find_element_by_xpath('//*[@id="cboxLoadedContent"]//form[@class="loginForm nbm"]//input[@name="password"]')
        elem.send_keys(password)
        elem.send_keys(Keys.RETURN)

    def login_authenticate(driver, username, password):
        elem = driver.find_element_by_name("email")
        elem.send_keys(username)
        elem = driver.find_element_by_name("password")
        elem.send_keys(password)
        elem.send_keys(Keys.RETURN)
