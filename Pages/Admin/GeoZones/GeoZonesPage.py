from selenium import webdriver


class GeoZonesPage:

    def __init__(self, driver):
        self.driver = driver
        self.URL: str = 'http://localhost/LiteCart/admin/?app=geo_zones&doc=geo_zones'
        self.GEO_ZONE_LINK: str = '//form[@name="geo_zones_form"]//table//td//a'

    def open_geo_zone_page(self):
        geo_zones_links = self.driver.find_elements_by_xpath(self.GEO_ZONE_LINK)
        for geo_zone_number, geo_zone_link in enumerate(geo_zones_links):
            if geo_zone_number % 2 > 0:
                geo_zone_link.click()
                self.driver.back()
                new_geo_zones_links = self.driver.find_elements_by_xpath(self.GEO_ZONE_LINK)
                for key ,val in enumerate(new_geo_zones_links):
                    if key % 2 > 0:
                        val.click()
                        self.driver.back()