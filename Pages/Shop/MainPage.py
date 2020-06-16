class MainPage:
    """xPath поля email"""

    EMAIL_INPUT: str = '//input[@name="email"]'

    """xPath поля пароль"""

    PASSWORD_INPUT: str = '//input[@name="password"]'

    """xPath кнопки "Войти" """

    LOGIN_BUTTON: str = '//button[@name="login"]'

    """URL страницы"""

    URL: str = 'http://localhost/LiteCart/en/'

    def __init__(self, driver) -> None:
        self.driver = driver

    """Логинется в магазин"""

    def login(self, email: str, password: str):
        self.driver.find_element_by_xpath(self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element_by_xpath(self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()
        return self
