import pytest
from app.api.filecloud import FileCloud
from utils.helper import *


@pytest.fixture(scope="session", autouse=True)
def setup():
    if not hasattr(pytest, "client"):
        pytest.client = dict()
    pytest.client["admin"] = FileCloud().get_instance("admin")
    pytest.client["user"] = FileCloud().get_instance("user")
    yield
    del pytest.client