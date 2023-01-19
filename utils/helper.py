import os
from dotenv import load_dotenv
import string
import random


def get_random_string(length):
    possible = string.ascii_lowercase
    return "".join([random.choice(possible) for i in range(length)])


def get_random_user_name():
    return get_random_string(10)


def get_random_email():
    return "{0}@{1}.{2}".format(get_random_string(8), get_random_string(5), get_random_string(3))

def get_random_password():
    return get_random_string(10)


load_dotenv()

config_dict = {}

config_file = "config.env"

with open(config_file, "r") as f:
    for line in f:
        line = line.split("=")
        config_dict[line[0].strip()] = line[1].strip()


def get_admin_credentials():
    user = os.environ.get("admin_user").strip()
    password = os.environ.get("admin_pass").strip()
    return user, password


def get_admin_login_url():
    return config_dict.get("base_url")+config_dict.get("admin_login_url")


def get_user_creation_url():
    return config_dict.get("base_url")+config_dict.get("user_creation_url")


def get_delete_user_url():
    return config_dict.get("base_url")+config_dict.get("user_deletion_url")

def get_user_login_url():
    return config_dict.get("base_url")+config_dict.get("user_login_url")

def get_ui_base_url():
    print("dict: ", config_dict)
    return config_dict.get("ui_base_url")

def get_ui_username():
    return os.environ.get("ui_user").strip()

def get_ui_password():
    return os.environ.get("ui_password").strip()