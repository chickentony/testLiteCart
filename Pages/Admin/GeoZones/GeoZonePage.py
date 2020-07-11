from selenium import webdriver


class GeoZonePage:

    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.GEO_ZONE_SELECTOR: str = '//table[@id="table-zones"]//td//select'
        self.OPTION = './/option'

    def get_zones(self):
        zones_info = self.driver.find_elements_by_xpath(self.GEO_ZONE_SELECTOR)
        zone_names = []
        for zone_number, zone in enumerate(zones_info):
            if zone_number % 2 == 0:
                # print(zone_number)
                zone_names.append(zone.find_element_by_xpath(self.OPTION).get_attribute('selected'))
                #     for res in result:
        #         if res.get_attribute('selected'):
        #             zone_names.append(res.text)
        # for zone_name in zone_names:
        #     if zone_name.get_attribute('selected'):
        print(zone_names)
