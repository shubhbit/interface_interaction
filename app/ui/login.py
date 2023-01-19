from app.ui.ui_base import UIBase
from selenium.webdriver.common.by import By

class LoginElements(object):
    USER_NAME = (By.XPATH, "//input[@id='user-name']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@type='submit']")
    SUCCESS_TEXT = "Swag Labs"

class Login(UIBase):
    def login(self, user, password):
        user_input = self.driver.find_element(*LoginElements.USER_NAME)
        user_input.send_keys(user)
        password_input = self.driver.find_element(*LoginElements.PASSWORD)
        password_input.send_keys(password)
        login_button = self.driver.find_element(*LoginElements.LOGIN_BUTTON)
        login_button.click()

    def verify_login(self):
        if LoginElements.SUCCESS_TEXT in self.driver.title:
            self.is_logged_in = True
        return self.is_logged_in
    


