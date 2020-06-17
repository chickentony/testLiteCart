import pytest
from selenium import webdriver
from Pages.Admin.LoginPage import LoginPage


@pytest.fixture()
def browser(request):
    browser = webdriver.Chrome()
    request.addfinalizer(browser.quit)
    return browser


def test_left_menu_sections(browser):
    login_page = LoginPage(browser)

    browser.get(login_page.URL)
    login_page.login('admin', 'admin')
