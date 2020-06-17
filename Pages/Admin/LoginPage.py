# from selenium import webdriver


class LoginPage:
    USERNAME_INPUT: str = '//input[@name="username"]'

    PASSWORD_INPUT: str = '//input[@name="password"]'

    LOGIN_BUTTON = '//button[@name="login"]'

    def __init__(self, driver):
        self.URL: str = 'http://localhost/LiteCart/admin/login.php'
        self.driver = driver

    def login(self, login: str, password: str):
        self.driver.find_element_by_xpath(self.USERNAME_INPUT).send_keys(login)
        self.driver.find_element_by_xpath(self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()
