from selenium import webdriver
from utils.helper import *


class UIBase(object):
    def __init__(self):
        self.is_logged_in = False
        self.base_url = get_ui_base_url()
        self.driver = webdriver.Firefox()
        self.driver.get(self.base_url)
    def close(self):
        self.driver.close()
