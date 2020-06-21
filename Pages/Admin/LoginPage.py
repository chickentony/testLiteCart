# TODO: Вынести в отдельный степ
class LoginPage:

    def __init__(self, driver):
        self.URL: str = 'http://localhost/LiteCart/admin/login.php'
        self.driver = driver
        self.USERNAME_INPUT: str = '//input[@name="username"]'
        self.PASSWORD_INPUT: str = '//input[@name="password"]'
        self.LOGIN_BUTTON = '//button[@name="login"]'

    """Логинется в админку"""
    def login(self, login: str, password: str) -> None:
        self.driver.find_element_by_xpath(self.USERNAME_INPUT).send_keys(login)
        self.driver.find_element_by_xpath(self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()
