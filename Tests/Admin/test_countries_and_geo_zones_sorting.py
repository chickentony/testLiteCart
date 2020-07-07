from Tests.browser_settings import init_browser
from Pages.Admin.LoginPage import LoginPage
from Pages.Admin.CountriesPage.Countries import Countries

browser = init_browser


# Проверяет что страны в спсике идут в алфавитном порядке
def test_countries_sorting(browser):
    login_page = LoginPage(browser)
    countries_page = Countries(browser)

    browser.get(login_page.URL)
    login_page.login('admin', 'admin')
    browser.get(countries_page.URL)
    countries_page.get_countries_name()

    countries_page.assert_countries_sorting()


# Проверяет что у стран, у которых число зон больше нуля, зоны отстортированы в алфавитном порядке
# ToDo: сейчас не оптимальная сборка информации о странах с зонами и возможно ассерт можно вынести отдельно
def test_zones_sorting_on_country_page(browser):
    login_page = LoginPage(browser)
    countries_page = Countries(browser)

    browser.get(login_page.URL)
    login_page.login('admin', 'admin')
    browser.get(countries_page.URL)
    countries_page.get_countries_with_zones()

    countries_page.open_countries_with_zones_and_check_zones_sorting()
