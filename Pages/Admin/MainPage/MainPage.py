class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.LEFT_MENU_SECTIONS: str = '//ul[@id="box-apps-menu"]//li[@id="app-"]'
        self.LEFT_MENU_SUBSECTIONS: str = '//ul[@class="docs"]//li'

    """Возвращает список пунктов левого меню"""
    def get_all_left_menu_sections(self) -> list:
        return self.driver.find_elements_by_xpath(self.LEFT_MENU_SECTIONS)

    """Возвращает список подпунктов левого меню"""
    def get_all_left_menu_subsection_items(self) -> list:
        return self.driver.find_elements_by_xpath(self.LEFT_MENU_SUBSECTIONS)

    """Кликает по всем пунктам и подпунктам левого меню и проверяет наличие заголовка на странице"""
    def click_on_all_left_menu_sections_and_check_page_headers(self) -> None:
        sections = self.get_all_left_menu_sections()
        for section_number, section in enumerate(sections):
            sections_new = self.get_all_left_menu_sections()
            sections_new[section_number].click()
            page_header = self.driver.find_element_by_xpath('//h1').text
            assert page_header
            subsections = self.get_all_left_menu_subsection_items()
            if len(subsections) > 0:
                for subsection_number, subsection in enumerate(subsections):
                    subsections_new = self.get_all_left_menu_subsection_items()
                    subsections_new[subsection_number].click()
                    # TODO: вынести в хелпер?
                    page_header = self.driver.find_element_by_xpath('//h1').text
                    assert page_header
