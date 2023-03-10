import pytest
from utils.helper import *

user, password = get_admin_credentials()


def get_user_data():
    username = get_random_user_name()
    email = get_random_email()
    password = get_random_password()
    return {"username": username, "displayname": username, "email": email, "password": password}



class TestAdmin:

    def test_admin_login(self):
        response = pytest.client["admin"].login_admin(
            user, password)
        assert response.status_code == 200

    @pytest.mark.parametrize("user,password,expected_code", [("invalid", "invalid", 400), ("invalid", password, 400), (user, "invalid", 400)])
    def test_invalid_credentials_login(self, user, password, expected_code):
        response = pytest.client["admin"].login_admin(user, password)
        assert response.status_code == expected_code

    def test_user_creation_deletion(self):
        pytest.client["admin"].login_admin(
            user, password)
        user_data = get_user_data()
        response = pytest.client["admin"].create_user(*list(user_data.values()))
        print(response.text)
        assert response.status_code == 200
        delete_res = pytest.client["admin"].delete_user(user_data['username'])
        print(delete_res.status_code)
        assert delete_res.status_code == 200
