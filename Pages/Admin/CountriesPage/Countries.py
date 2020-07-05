from selenium import webdriver
from Pages.Admin.CountriesPage.Country import Country


class Countries:
    # country_page: object = Country()

    def __init__(self, driver) -> None:
        self.driver = driver
        # URL Страницы
        self.URL: str = 'http://localhost/LiteCart/admin/?app=countries&doc=countries'
        # Ссылка на страницу страны
        self.COUNTRY_HREF: str = '//form[@name="countries_form"]//td//a'
        # Спсиок для названий стран
        self.countries_names: list = []
        self.COUNTRY_ROW: str = '//form[@name="countries_form"]//tr[@class="row"]'
        self.COUNTRY_EDIT: str = './/td[string-length(text()) > 0]'
        self.countries_with_zones_links: list = []
        self.country_page: Country = Country(driver)

    # Заполняет список названиями стран
    def get_countries_name(self) -> None:
        countries_names = self.driver.find_elements_by_xpath(self.COUNTRY_HREF)
        if len(countries_names) > 0:
            for country_name in countries_names:
                if country_name.text != '':
                    self.countries_names.append(country_name.text)

    def get_countries_with_zones(self):
        countries_info = self.driver.find_elements_by_xpath(self.COUNTRY_ROW)
        for value in countries_info:
            res = value.find_elements_by_xpath(self.COUNTRY_EDIT)
            for v in res:
                if v.get_property('cellIndex') == 5 and v.text != '0':
                    self.countries_with_zones_links.append(value.find_element_by_xpath('.//a').get_attribute('href'))

    def open_countries_with_zones(self):
        for link in self.countries_with_zones_links:
            self.driver.get(link)
            result = self.country_page.get_zones()
            self.country_page.assert_zones_sorting(result)

    # Проверяет что полученный спсиок со странами равен отсортированному (по алфавиту) спсику со странами
    def assert_countries_sorting(self) -> None:
        sorted_counties_name = sorted(self.countries_names)
        if self.countries_names == sorted_counties_name:
            print('Countries sorted in alphabet order')
        else:
            raise AssertionError('Check countries sorting')
