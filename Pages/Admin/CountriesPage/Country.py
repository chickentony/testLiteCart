from selenium import webdriver


class Country:

    def __init__(self, driver):
        self.driver = driver
        self.ZONE_TABLE: str = '//table[@id="table-zones"]//tr'
        self.zones_names: list = []

    def get_zones(self):
        zones_info = self.driver.find_elements_by_xpath(self.ZONE_TABLE)
        result = []
        for zone in zones_info:
            zones_name = zone.find_elements_by_xpath('.//td')
            for z in zones_name:
                if z.get_property('cellIndex') == 2:
                    result.append(z.text)
                    # self.zones_names.append(z.text)
        return result

    def assert_zones_sorting(self, zones_names: list):
        formatted_zones_names = list(filter(None, zones_names))
        # print(foramted_zones_names)
        sorted_zones_names = sorted(formatted_zones_names)
        # print(zones_names, sorted_zones_names, end='')
        if formatted_zones_names == sorted_zones_names:
            print('Zones sorted in alphabet order')
        else:
            raise AssertionError('Check zones sorting')
