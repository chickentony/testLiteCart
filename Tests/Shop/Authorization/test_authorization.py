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
    success_auth_text = 'You are now logged in as Антон Миролюбов.'

    browser.get(main_page.URL)
    main_page.login('test@test.ru', '12345')
    assert (success_auth_text in browser.page_source)
