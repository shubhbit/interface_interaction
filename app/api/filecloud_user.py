from app.api.filecloud_base import FileCloudBase
from utils.helper import *
import requests


class FileCloudUser(FileCloudBase):
    def user_login(self, userid, password):
        user_login_url = get_user_login_url()
        user_login_url_query = self.build_url(
            user_login_url, {"userid": userid, "password": password})
        response = requests.post(user_login_url_query)
        if response.status_code == 200:
            self.cookies = response.cookies
        return response
