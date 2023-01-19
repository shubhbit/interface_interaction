import pytest
from app.ui.login import Login

@pytest.fixture(scope="function")
def ui():
    ui_handle = Login()
    yield ui_handle
    ui_handle.close()
    del ui_handle