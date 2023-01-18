import pytest
from app.api.filecloud import FileCloud

@pytest.fixture
def init_test(scope="session", autouse=True):
    print("fixture called....")
    if not hasattr(pytest, "file_client"):
        pytest.file_client = dict()
    pytest.file_client["admin"] = FileCloud().get_instance("admin")
    pytest.file_client["user"] = FileCloud().get_instance("user")
    yield
    del pytest.client