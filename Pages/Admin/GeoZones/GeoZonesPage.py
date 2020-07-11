from selenium import webdriver
from Pages.Admin.GeoZones import GeoZonePage

class GeoZonesPage:

    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()
        self.geo_zone_page = GeoZonePage.GeoZonePage(driver)
        self.URL: str = 'http://localhost/LiteCart/admin/?app=geo_zones&doc=geo_zones'
        self.GEO_ZONE_LINK: str = '//form[@name="geo_zones_form"]//table//td//a'

    def get_geo_zones_links(self):
        geo_zones_links = self.driver.find_elements_by_xpath(self.GEO_ZONE_LINK)
        result = []
        for geo_zone_number, geo_zone_link in enumerate(geo_zones_links):
            if geo_zone_number % 2 > 0:
                result.append(geo_zone_link.get_attribute('href'))

        return result

    def open_geo_zone_page(self):
        geo_zones_links = self.get_geo_zones_links()
        for geo_zone_link in geo_zones_links:
            self.driver.get(geo_zone_link)
            self.geo_zone_page.get_zones()
