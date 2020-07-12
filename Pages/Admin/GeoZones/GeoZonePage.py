from selenium import webdriver


class GeoZonePage:

    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.GEO_ZONE_SELECTOR: str = '//table[@id="table-zones"]//td//select[not(@class="select2-hidden-accessible")]'
        self.OPTION_TAG = './/option'

    def get_zones(self):
        zones_info = self.driver.find_elements_by_xpath(self.GEO_ZONE_SELECTOR)
        zone_names = ''
        result = []
        for zone in zones_info:
            zone_names = zone.find_elements_by_xpath(self.OPTION_TAG)
        for i in zone_names:
            if i != '-- All Zones --':
                result.append(i.text)

        return result

    @staticmethod
    def assert_zone_sorting(zone_names):
        sorted_zone_names = sorted(zone_names)
        if zone_names == sorted_zone_names:
            print('\n' + 'Zones sorted in alphabet order')
        else:
            raise AssertionError('Check zones sorting')
