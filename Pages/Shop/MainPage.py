from selenium.common.exceptions import NoSuchElementException
from Pages.Shop.Product.ProductPage import ProductPage
from selenium import webdriver

class MainPage:
    # ToDo рефакторинг
    """xPath поля email"""
    EMAIL_INPUT: str = '//input[@name="email"]'

    """xPath поля пароль"""
    PASSWORD_INPUT: str = '//input[@name="password"]'

    """xPath кнопки "Войти" """
    LOGIN_BUTTON: str = '//button[@name="login"]'

    """URL страницы"""
    URL: str = 'http://localhost/LiteCart/en/'

    """Словарь со стикерами продуктов"""
    stickers: dict = {}

    def __init__(self, driver) -> None:
        self.driver = driver
        # self.driver = webdriver.Chrome()
        self.LOGOTYPE_CONTAINER: str = '//div[@id="logotype-wrapper"]'
        self.PRODUCT_IMAGES_CONTAINER: str = '//div[@class="image-wrapper"]'
        self.STICKER_CONTAINER: str = './/div[@class="sticker sale"]'
        # Comment this
        self.FIRST_CAMPAIGN_PRODUCT_HREF: str = '(//div[@id="box-campaigns"]//li//a)[1]'
        self.product_page = ProductPage(driver)

    """Логинется в магазин"""
    def login(self, email: str, password: str):
        self.driver.find_element_by_xpath(self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element_by_xpath(self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()
        return self

    """Получает список всех картинок товаров на главной страницы"""
    def _get_all_products_images(self) -> list:
        return self.driver.find_elements_by_xpath(self.PRODUCT_IMAGES_CONTAINER)

    """Получает все стикеры с картинок продуктов на главной странице"""
    def get_all_stickers_from_product_images(self) -> None:
        images = self._get_all_products_images()
        for key, image in enumerate(images):
            try:
                # ToDo: Сейчас первый ключ для элемента меняется при кажом вызове словаря, нужно переделать
                self.stickers[key] = image.find_element_by_xpath(self.STICKER_CONTAINER).text
            except NoSuchElementException:
                continue

    def open_product_page(self, product_link: str):
        self.driver.find_element_by_xpath(product_link).click()

    """Проверка наличия стикеров"""
    def assert_stickers(self) -> None:
        assert self.stickers
        for product_number, product_sticker in self.stickers.items():
            print('product ' + str(product_number) + ' has sticker ' + product_sticker)
