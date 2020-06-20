# from selenium import webdriver


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        # self.LEFT_MENU_ITEMS

    def get_all_left_menu_items(self):
        left_menu = self.driver.find_element_by_xpath('//ul[@id="box-apps-menu"]')
        return left_menu.find_elements_by_xpath('.//li[@id="app-"]')

    def click_on_all_left_menu_sections(self):
        sections = self.get_all_left_menu_items()
        for key, value in enumerate(sections):
            sections_new = self.driver.find_elements_by_xpath('//li[@id="app-"]')
            sections_new[key].click()
            page_header = self.driver.find_element_by_xpath('//h1').text
            assert page_header
            subsections = self.driver.find_elements_by_xpath('//ul[@class="docs"]//li')
            if len(subsections) > 0:
                for k, v in enumerate(subsections):
                    subsections_new = self.driver.find_elements_by_xpath('//ul[@class="docs"]//li')
                    subsections_new[k].click()
                    page_header = self.driver.find_element_by_xpath('//h1').text
                    assert page_header
