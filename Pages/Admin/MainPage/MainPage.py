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
#           Проблема в том, что при кажом клике id элементов меняются, а значит элементы в изначальном массиве не подхо-
#             дят, нужно понять что с этим можно сделать
