from Tests.browser_settings import init_browser
from Pages.Admin.LoginPage import LoginPage
from Pages.Admin.GeoZones import GeoZonesPage

browser = init_browser


# Для каждой страны на странице зон, проверяет сортировку всех гео-зон
def test_geo_zones_sorting(browser):
    login_page = LoginPage(browser)
    geo_zones_page = GeoZonesPage.GeoZonesPage(browser)

    browser.get(login_page.URL)
    login_page.login('admin', 'admin')
    browser.get(geo_zones_page.URL)
    geo_zones_page.get_geo_zones_links()

    geo_zones_page.open_geo_zone_page_and_check_zones_sorting()
