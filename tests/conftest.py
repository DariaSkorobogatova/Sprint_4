import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    wd = webdriver.Firefox()
    wd.maximize_window()
    wd.implicitly_wait(30)
    yield wd
    wd.quit()
