from Pages.Admin.LoginPage import LoginPage
from Pages.Admin.MainPage.MainPage import MainPage
from Tests.browser_settings import init_browser

browser = init_browser


def test_page_headers_in_left_menu_sections(browser):
    login_page = LoginPage(browser)
    main_page = MainPage(browser)

    browser.get(login_page.URL)
    login_page.login('admin', 'admin')

    main_page.click_on_all_left_menu_sections_and_check_page_headers()
