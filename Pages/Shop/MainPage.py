from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class MainPage:
    """xPath поля email"""
    EMAIL_INPUT: str = '//input[@name="email"]'

    """xPath поля пароль"""
    PASSWORD_INPUT: str = '//input[@name="password"]'

    """xPath кнопки "Войти" """
    LOGIN_BUTTON: str = '//button[@name="login"]'

    """URL страницы"""
    URL: str = 'http://localhost/LiteCart/en/'

    stickers: dict = {}

    def __init__(self, driver) -> None:
        self.driver = driver

    """Логинется в магазин"""
    def login(self, email: str, password: str):
        self.driver.find_element_by_xpath(self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element_by_xpath(self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()
        return self

    def _get_all_products_images(self) -> list:
        return self.driver.find_elements_by_xpath('//div[@class="image-wrapper"]')

    def get_all_product_images(self):
        images = self._get_all_products_images()
        for key, image in enumerate(images):
            try:
                image.find_element_by_xpath('.//div[@class="sticker sale"]')
                self.stickers[key] = image.find_element_by_xpath('.//div[@class="sticker sale"]').text
            except NoSuchElementException:
                continue
        print(self.stickers)

    def assert_stickers(self):
        for product_number, product_sticker in self.stickers.items():
            print(product_number)
            # print( "has sticker" + product_sticker)