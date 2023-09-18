import time
import unittest

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from framework.pages.login_page import LoginPage


class Login_test(unittest.TestCase):
    def test_valid(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get('https://practicetestautomation.com/practice-test-login/')
        driver.maximize_window()
        time.sleep(2)


        lp = LoginPage(driver)
        lp.login_pratice('student', 'password123')

        driver.close()