from Tests.browser_settings import init_browser
from Pages.Admin.LoginPage import LoginPage
from Pages.Admin.CountriesPage.Countries import Countries

browser = init_browser


def test_check_countries_sorting(browser):
    login_page = LoginPage(browser)
    countries_page = Countries(browser)

    browser.get(login_page.URL)
    login_page.login('admin', 'admin')
    browser.get(countries_page.URL)
    countries_page.get_countries_name()

    countries_page.assert_countries_sorting()
