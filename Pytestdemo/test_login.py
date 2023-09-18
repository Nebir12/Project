import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import

@pytest.yield_fixture()
def browser_config():
    global driver

    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    driver.get('https://practicetestautomation.com/practice-test-login/')
    driver.maximize_window()
    time.sleep(3)

    yield
    driver.close()

@pytest.mark.order(1)
@pytest.mark.valid
def test_login_001_valid(browser_config):
    username_btn = driver.find_element(By.ID, 'username')
    username_btn.send_keys('student')

    password_btn = driver.find_element(By.NAME, 'password')
    password_btn.send_keys('Password123')

    submit_btn = driver.find_element(By.ID, 'submit')
    submit_btn.click()

@pytest.mark.order(2)
@pytest.mark.invalid
def test_login_002_invalid(browser_config):
    username_btn = driver.find_element(By.ID, 'username')
    username_btn.send_keys('student')

    password_btn = driver.find_element(By.NAME, 'password')
    password_btn.send_keys('Password12kih3')

    submit_btn = driver.find_element(By.ID, 'submit')
    submit_btn.click()


@pytest.mark.order(3)
@pytest.mark.skip('undone work')
@pytest.mark.invalid
def test_login_003_invalid(browser_config):
    username_btn = driver.find_element(By.ID, 'username')
    username_btn.send_keys('')

    password_btn = driver.find_element(By.NAME, 'password')
    password_btn.send_keys('')

    submit_btn = driver.find_element(By.ID, 'submit')
    submit_btn.click()

@pytest.mark.order(4)
@pytest.mark.invalid
def test_login_004_invalid(browser_config):

    username_btn = driver.find_element(By.ID, 'username')
    username_btn.send_keys('khkghj')

    password_btn = driver.find_element(By.NAME, 'password')
    password_btn.send_keys('hgdhchg')

    submit_btn = driver.find_element(By.ID, 'submit')
    submit_btn.click()

@pytest.mark.order(5)
@pytest.mark.valid
def test_login_005_valid(browser_config):
    username_btn = driver.find_element(By.ID, 'username')
    username_btn.send_keys('student')

    password_btn = driver.find_element(By.NAME, 'password')
    password_btn.send_keys('Password123')

    submit_btn = driver.find_element(By.ID, 'submit')
    submit_btn.click()

