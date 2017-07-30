"""
This template is designed by Ankit Kumar Singh<remove this line>
Date: '''Date and Time of writing this code'
Author: ''Your name''
Place: ''Place of writing this code''
Purpose: ''define purpose of this test''
Browser : ''Browser that will cover test''
"""

'''
All necessary imports are present here
'''
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
import time
import unittest
from LoginPage import Login #import this only if testing requires you to Log In
from PathCreator import Path 

'''
Variable path stores path to chromedriver
'''
path = Path.returnPath()


'''
Change class name accordingly but make sure class name and file name are
exactly same(Even the cases of letters)
There will only be one class in a test file which inherits 'unittest.TestCase'
class from 'unittest' module
'''
class TestTemplate(unittest.TestCase):

    '''
    This is setUp method
    This method is the first to execute and as the name signifies, it sets
    up the environment for test to take place.
    For eg. A test which requires login should contain login part in this
    method and actual testing code in the test method.

    - @classmethod is used to make sure that webdriver closes the browser after
    every set of tests to start fresh.

    - self is used for class variables so variables with self attached to them
    can be accessed anywhere inside the class
        
    - driver is initialised by calling Chrome method of selenium webdriver
    with path of chromedriver as an argument.

    - driver.get(<webpage address>) will open the browser with specified web
    address

    - email and pwd are variables used for storing credentials that will be
    used during login

    - maximize_windows() maximizes the browser window

    - implicitly_wait(10) is a way of saying that webdriver should wait
    atleast 10 seconds in case it doesn't find what it is looking for.
    This is necessary since internet is not stable everytime and delay in
    page loads may declare a test as failed when it is not.
    This can be adjusted according to the speed of your internet connection.

    - 'Login' is a class in a file named 'LoginPage.py' and 'login()' is a
    method inside that class. 'login()' takes in 3 arguments viz. webdriver
    object i.e. self.driver, email and password. This wil log you in the
    website. Make sure to use self.driver.get("https://learn.spayee.com/store")
    when you use 'login()' because login can be done from this page only.
    If you dont want to login, then this #line a can be removed along with
    self.email and self.pwd.
    '''
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(path)
        self.driver.get("https://learn.spayee.com/store")
        self.email = "ankitsingh095@outlook.com"
        self.pwd = "spayee123"
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        Login.login(self.driver, self.email, self.pwd) #line a

    '''
    Below are two test method
    A test is defined in method starting with word 'test_'.
    For eg. test_login(), test_signup() etc.
    Mutiple tests can be present in a single class by creating a seperate
    method for each test.

    NOTE - In case of multiple tests in a single class, the order of test
    execution is alphabetical w.r.t name of method.
    '''
    def test_1(self):
        '''
        Code here will be the actual test code
        '''

    def test_2(self):
        '''
        This method is created to show how multiple test can be written
        in one class. Use this to add second test else remove it. 
        '''

    '''
    This is tearDown method.
    Just like setUp method creates the enviroment for test to execute,
    this method does the reverse of it. It cleans the enviroment that
    was setup for test. This is done by using 'quit()' method.
    '''
    @classmethod
    def tearDownClass(self):
        self.driver.quit()


'''
This is the driver of any python program.
Python program starts executing from this line.
Leave these lines as it is.
unittest.main() starts the execution of tests.
'''
if __name__ == "__main__":
    unittest.main()
