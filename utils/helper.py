import os
from dotenv import load_dotenv

load_dotenv()

config_dict = {}

config_file = "config.env"

with open(config_file, "r") as f:
    for line in f:
        line = line.split("=")
        config_dict[line[0]] = line[1]

def get_admin_credentials():
    user = os.environ.get("admin_user")
    password = os.environ.get("admin_pass")
    return user, password

def get_admin_login_url():
    return config_dict.get("base_url")+config_dict.get("admin_login_url")


def get_user_creation_url():
    return config_dict.get("base_url")+config_dict.get("user_creation_url")


def get_delete_user_url():
    return config_dict.get("base_url")+config_dict.get("user_deletion_url")
