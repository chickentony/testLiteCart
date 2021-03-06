import pytest
from selenium import webdriver


@pytest.fixture()
def init_browser(request):
    browser = webdriver.Chrome()
    request.addfinalizer(browser.quit)
    return browser
