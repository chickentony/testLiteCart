import pytest
from selenium import webdriver
from Pages.Shop.MainPage import MainPage


@pytest.fixture()
def browser(request):
    browser = webdriver.Chrome()
    request.addfinalizer(browser.quit)
    return browser


def test_success_auth(browser):
    main_page = MainPage(browser)

    browser.get(main_page.URL)
