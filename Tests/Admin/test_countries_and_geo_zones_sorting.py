from Tests.browser_settings import init_browser
from Pages.Admin.LoginPage import LoginPage
from Pages.Admin.CountriesPage.Countries import Countries

browser = init_browser


# Проверяет что страны в спсике идут в алфавитном порядке
def test_check_countries_sorting(browser):
    login_page = LoginPage(browser)
    countries_page = Countries(browser)

    browser.get(login_page.URL)
    login_page.login('admin', 'admin')
    browser.get(countries_page.URL)
    countries_page.get_countries_name()

    countries_page.assert_countries_sorting()


def test_check_zones_sorting_on_country_page(browser):
    login_page = LoginPage(browser)
    countries_page = Countries(browser)

    browser.get(login_page.URL)
    login_page.login('admin', 'admin')
    browser.get(countries_page.URL)
    countries_page.get_countries_with_zones()
    countries_page.open_countries_with_zones()

    # countries_page.country_page.assert_zones_sorting()