import sys
import os
import pytest

test_report_path = os.path.dirname(__file__) + '\\reports'
test_path = os.path.dirname(__file__)
sys.path.append(test_path)
sys.path.append(test_report_path)

from LoginPage import Login_Page
from TestData import *

class TestLoginPage:
    @pytest.fixture(autouse=True)
    def test_setup(self, chrome_driver):
        global login_page
        login_page = Login_Page(chrome_driver)
        login_page.load_page()
        yield

    def test_get_title(self):
        assert Login_Title == login_page.get_page_title()

    def test_login_failed(self):
        login_page.get_input_username().send_keys(Login_UserName_Failed)
        login_page.get_input_password().send_keys(Login_Password_Failed)
        login_page.get_button_login().click()
        assert Login_Failed_Message == login_page.get_login_failed_message()

    def test_login(self):
        login_page.get_input_username().send_keys(Login_UserName)
        login_page.get_input_password().send_keys(Login_Password)
        login_page.get_button_login().click()
        pass

    def test_login_failed_yaml(self):
        login_page.get_input_username().send_keys(Login_UserName_Failed_YAML)
        login_page.get_input_password().send_keys(Login_Password_Failed_YAML)
        login_page.get_button_login().click()
        assert Login_Failed_Message_YAML == login_page.get_login_failed_message()

    def test_login_yaml(self):
        login_page.get_input_username().send_keys(Login_UserName_YAML)
        login_page.get_input_password().send_keys(Login_Password_YAML)
        login_page.get_button_login().click()
        pass