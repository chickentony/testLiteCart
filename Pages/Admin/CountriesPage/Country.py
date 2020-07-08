class Country:

    # Инициализация браузера и элементов на странице
    def __init__(self, driver):
        # Инициализация браузера
        self.driver = driver
        # Строка с информацией о зоне в таблице зон
        self.ZONE_TABLE_ROW: str = '//table[@id="table-zones"]//tr'
        # Контейнер с именем страны
        self.ZONE_NAME_CELL: str = './/td'

    # Получает название всех зон, которые есть у страны
    def get_zones_name(self) -> list:
        zones_info = self.driver.find_elements_by_xpath(self.ZONE_TABLE_ROW)
        result = []
        for zone_info in zones_info:
            zones_names = zone_info.find_elements_by_xpath(self.ZONE_NAME_CELL)
            for zone_name in zones_names:
                if zone_name.get_property('cellIndex') == 2:
                    result.append(zone_name.text)

        return result

    @staticmethod
    # Сравнивает спсисок названий зон с отсортированным спсиском названий зон
    def assert_zones_sorting(zones_names: list) -> None:
        zones_names_without_whitespaces = list(filter(None, zones_names))
        sorted_zones_names = sorted(zones_names_without_whitespaces)
        if zones_names_without_whitespaces == sorted_zones_names:
            print('\n' + 'Zones sorted in alphabet order')
        else:
            raise AssertionError('Check zones sorting')
