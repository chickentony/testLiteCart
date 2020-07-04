# from selenium import webdriver

class Countries:

    def __init__(self, driver) -> None:
        self.driver = driver
        self.URL: str = 'http://localhost/LiteCart/admin/?app=countries&doc=countries'
        self.COUNTRY_HREF: str = '//form[@name="countries_form"]//td//a'

    def get_countries_name(self):
        countries_names = self.driver.find_elements_by_xpath(self.COUNTRY_HREF)
        result = []
        if len(countries_names) > 0:
            for country_name in countries_names:
                if country_name.text != '':
                    result.append(country_name.text)

        return result

    def assert_countries_sorting(self):
        countries_names = self.get_countries_name()
        sorted_counties_name = sorted(countries_names)
        if countries_names == sorted_counties_name:
            print('Countries are ok')
        else:
            print('Countries are not ok')
