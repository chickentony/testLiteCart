from Pages.Admin.GeoZones import GeoZonePage


class GeoZonesPage:

    # Инициализация браузера и элементов на странице
    def __init__(self, driver) -> None:
        self.driver = driver
        self.geo_zone_page = GeoZonePage.GeoZonePage(driver)
        # URL страницы
        self.URL: str = 'http://localhost/LiteCart/admin/?app=geo_zones&doc=geo_zones'
        # Ссылка на страницу конкретной гео-зоны
        self.GEO_ZONE_LINK: str = '//form[@name="geo_zones_form"]//table//td//a'

    # Возвращает список ссылок на страницы гео-зон
    def get_geo_zones_links(self) -> list:
        geo_zones_links = self.driver.find_elements_by_xpath(self.GEO_ZONE_LINK)
        result = []
        for geo_zone_number, geo_zone_link in enumerate(geo_zones_links):
            if geo_zone_number % 2 > 0:
                result.append(geo_zone_link.get_attribute('href'))

        return result

    # Переходит на каждую страницу зоны, берет все зоны, котоыре есть на странице и проверяет их сортировку
    def open_geo_zone_page_and_check_zones_sorting(self):
        geo_zones_links = self.get_geo_zones_links()
        for geo_zone_link in geo_zones_links:
            self.driver.get(geo_zone_link)
            geo_zones = self.geo_zone_page.get_zones()
            geo_zones_selected_names = self.geo_zone_page.get_zones_names(geo_zones)
            self.geo_zone_page.assert_zones_sorting(geo_zones_selected_names)
