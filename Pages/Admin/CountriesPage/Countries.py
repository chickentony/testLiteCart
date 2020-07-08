from Pages.Admin.CountriesPage.Country import Country


class Countries:

    # Инициализация браузера и элементов на странице
    def __init__(self, driver) -> None:
        self.driver = driver
        # URL Страницы
        self.URL: str = 'http://localhost/LiteCart/admin/?app=countries&doc=countries'
        # Ссылка на страницу страны
        self.COUNTRY_HREF: str = '//form[@name="countries_form"]//td//a'
        # Спсиок для названий стран
        self.countries_names: list = []
        # Строка с информацие о стране
        self.COUNTRY_ROW: str = '//form[@name="countries_form"]//tr[@class="row"]'
        # Ячейка со значением в строке с информацие о стране
        self.INFORMATION_CELL: str = './/td[string-length(text()) > 0]'
        # Список стран у которых есть хотя бы одна зона
        self.countries_with_zones_links: list = []
        # Контейнер с ссылкой
        self.COUNTRY_LINK_CONTAINER: str = './/a'
        # Страница страны
        self.country_page: Country = Country(driver)

    # Заполняет список названиями стран
    def get_countries_name(self) -> None:
        countries_names = self.driver.find_elements_by_xpath(self.COUNTRY_HREF)
        if len(countries_names) > 0:
            for country_name in countries_names:
                if country_name.text != '':
                    self.countries_names.append(country_name.text)

    # Заполняет список стран с зонами, проверяется по значению количества зон в соответствующем поле
    def get_countries_with_zones(self) -> None:
        countries_info = self.driver.find_elements_by_xpath(self.COUNTRY_ROW)
        for country_info in countries_info:
            detailed_counties_info = country_info.find_elements_by_xpath(self.INFORMATION_CELL)
            for detailed_country_info in detailed_counties_info:
                if detailed_country_info.get_property('cellIndex') == 5 and detailed_country_info.text != '0':
                    self.countries_with_zones_links.append(
                        country_info.find_element_by_xpath(self.COUNTRY_LINK_CONTAINER).get_attribute('href')
                    )

    # Открывает ссылку на страну с зонами и проверяет сортировку этих зон
    def open_countries_with_zones_and_check_zones_sorting(self) -> None:
        for link in self.countries_with_zones_links:
            self.driver.get(link)
            zones_names = self.country_page.get_zones_name()
            self.country_page.assert_zones_sorting(zones_names)

    # Проверяет что полученный спсиок со странами равен отсортированному (по алфавиту) спсику со странами
    def assert_countries_sorting(self) -> None:
        sorted_counties_name = sorted(self.countries_names)
        if self.countries_names == sorted_counties_name:
            print('Countries sorted in alphabet order')
        else:
            raise AssertionError('Check countries sorting')
