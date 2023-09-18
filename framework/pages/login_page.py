from selenium.webdriver.common.by import By


class LoginPage():

    def __init__(self, driver):
        self.driver = driver



    def login_pratice(self , username, password):
        username_btn = self.driver.find_element(By.ID, 'username')
        password_btn = self.driver.find_element(By.NAME, 'password')
        submit_btn = self.driver.find_element(By.ID, 'submit')

        password_btn.clear()
        password_btn.send_keys(password)

        username_btn.clear()
        username_btn.send_keys(username)

        submit_btn.click()


