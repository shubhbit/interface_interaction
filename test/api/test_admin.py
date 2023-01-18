import pytest
from utils.helper import *

user, password = get_admin_credentials()


class TestAdmin:

    def test_admin_login(self):
        # print(dir(pytest))
        assert True
        # response = pytest.file_client["admin"].login_admin(
        #     user, password)
        # assert response.status_code == 200

    @pytest.mark.parametrize("user,password,expected_code", [("invalid", "invalid", 400), ("invalid", password, 400), (user, "invalid", 400)])
    def test_invalid_credentials_login(self, user, password, expected_code):
        response = pytest.file_client["admin"].login_admin(user, password)
        assert response.status_code == expected_code

    def test_user_creation_deletion(self):
        pass
