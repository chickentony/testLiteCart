import pytest
from selenium import webdriver
from Pages.Admin.LoginPage import LoginPage
from Pages.Admin.MainPage.MainPage import MainPage


@pytest.fixture()
def browser(request):
    browser = webdriver.Chrome()
    request.addfinalizer(browser.quit)
    return browser


def test_left_menu_sections(browser):
    login_page = LoginPage(browser)
    main_page = MainPage(browser)

    browser.get(login_page.URL)
    login_page.login('admin', 'admin')
    main_page.click_on_all_left_menu_sections()
