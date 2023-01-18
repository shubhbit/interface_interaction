import requests
from app.api.filecloud_base import FileCloudBase
from utils.helper import *


class FileCLoudAdmin(FileCloudBase):

    def login_admin(self, user, password):
        admin_login_url = get_admin_login_url()
        login_url = self.build_url(admin_login_url, locals())
        response = requests.post(login_url)
        if response.status_code == 200:
            self.cookies = response.cookies
        return response

    @FileCloudBase.authenticated
    def create_user(self, username, displayname, email, password, authtype=0, status=1):
        create_user_url = get_user_creation_url()
        create_user_url_query = self.build_url(create_user_url, locals())
        response = requests.post(create_user_url_query, cookies=self.cookies)
        return response

    @FileCloudBase.authenticated
    def delete_user(self, profile):
        delete_user_url = get_delete_user_url()
        delete_user_query_url = self.build_url(delete_user_url, locals())
        response = requests.post(delete_user_query_url, cookies=self.cookies)
        return response
