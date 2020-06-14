class MainPage:

    EMAIL_INPUT: str = '//input[@name="email"]'

    PASSWORD_INPUT: str = '//input[@name="password"]'

    URL: str = 'http://localhost/LiteCart/en/'

    def __init__(self, driver):
        self.driver = driver

    def login(self, email: str, password: str):
        self.driver.find_element_by_xpath()
