

import time
import unittest

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from framework.pages.login_page import LoginPage
from framework.utils import excel_utils


class LoginTest(unittest.TestCase):

    def test_login(self):
        driver =webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(3)

        # Excel implementation
        file = 'C:\\pythonProject7\\framework\\data\\login_dara.xlsx'
        sheet = 'Sheet1'

        number_of_rows = excel_utils.get_row_count(file, sheet)

        for r in range(2, number_of_rows + 1):
            username = excel_utils.read_data(file, sheet, r, 1)
            password = excel_utils.read_data(file, sheet, r, 2)

            lp = LoginPage(driver)
            lp.login_pratice(username, password)

        driver.close()