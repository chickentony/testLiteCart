class GeoZonePage:

    # Инициализация браузера и элементов на странице
    def __init__(self, driver) -> None:
        # self.driver = webdriver.Chrome()
        # Инициализация браузера
        self.driver = driver
        # Селектор с гео зонами
        self.GEO_ZONE_SELECTOR: str = '//table[@id="table-zones"]//td//select[not(@class="select2-hidden-accessible")]'
        # Тег <option>
        self.OPTION_TAG = './/option'

    # Возвращает список объектов элементов выбранных зон из выпадающего списка гео-зон
    # ToDo: костыль с пустой переменно или нет? Возможно нужен рефакторинг.
    def get_zones(self) -> list:
        zones = self.driver.find_elements_by_xpath(self.GEO_ZONE_SELECTOR)
        result = ''
        for zone in zones:
            result = zone.find_elements_by_xpath(self.OPTION_TAG)

        return result

    @staticmethod
    # Возвращает список имен выбранных зон
    def get_zone_names(zone_names: list) -> list:
        result = []
        for zone_name in zone_names:
            if zone_name.text != '-- All Zones --':
                result.append(zone_name.text)

        return result

    @staticmethod
    # Сравнивает спсисок названий зон с отсортированным спсиском названий зон
    def assert_zone_sorting(zone_names: list) -> None:
        sorted_zone_names = sorted(zone_names)
        if zone_names == sorted_zone_names:
            print('\n' + 'Zones sorted in alphabet order')
        else:
            raise AssertionError('Check zones sorting')
