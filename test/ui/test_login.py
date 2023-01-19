import pytest
from utils.helper import *

class TestLogin:
    def test_user_login_ui(self, ui):
        user_name = get_ui_username()
        password = get_ui_password()
        ui.login(user_name, password)
        assert ui.verify_login()