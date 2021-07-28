import sys
import os

sys.path.append(os.path.dirname(__file__))

from selenium.webdriver.common.by import By
from LoginPageLocators import *

class Login_Page():
    def __init__(self, _driver):
        self.by = By.XPATH
        global driver
        driver = _driver

    def load_page(self):
        driver.get(Login_Url)
        global by
        by = self.by
        self.page_title = driver.title
        self.input_username = driver.find_element(by, Login_UserName)
        self.input_password = driver.find_element(by, Login_Password)
        self.button_login = driver.find_element(by, Login_Button)

    def get_page_url():
        return Login_Url

    def get_page_title(self):
        return self.page_title

    def get_input_username(self):
        return self.input_username

    def get_input_password(self):
        return self.input_password

    def get_button_login(self):
        return self.button_login

    def get_login_failed_message(self):
        return driver.find_element(by, Login_Failed_Message).text