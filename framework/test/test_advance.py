import time
import unittest

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from framework.pages.login_page import LoginPage
from framework.utils import excel_utils


class Login_test(unittest.TestCase):
    def test_valid(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get('https://practicetestautomation.com/practice-test-login/')
        driver.maximize_window()
        time.sleep(2)


        file = "C:\\pythonProject7\\framework\\data\\login_data.xlsx"
        sheet = 'Sheet1'

        number_of_row = excel_utils.get_row_count(file, sheet)


        number_of_column = excel_utils.get_column_count(file, sheet)


        data = excel_utils.read_data(file, sheet, 1, 1)
        print(data)


        for r in range(2, number_of_row + 1):
            username = excel_utils.read_data(file, sheet, r, 1)
            password = excel_utils.read_data(file, sheet, r, 2)

            lp = LoginPage(driver)
            lp.login_pratice(username, password)

        driver.close()