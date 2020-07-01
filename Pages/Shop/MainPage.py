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

    """Словарь со стикерами продуктов"""
    stickers: dict = {}

    def __init__(self, driver) -> None:
        self.driver = driver
        self.LOGOTYPE_CONTAINER: str = '//div[@id="logotype-wrapper"]'
        self.PRODUCT_IMAGES_CONTAINER: str = '//div[@class="image-wrapper"]'
        self.STICKER_CONTAINER: str = './/div[@class="sticker sale"]'

    """Логинется в магазин"""
    def login(self, email: str, password: str):
        self.driver.find_element_by_xpath(self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element_by_xpath(self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()
        return self

    """Получает список всех картинок товаров с главной страницы"""
    def _get_all_products_images(self) -> list:
        return self.driver.find_elements_by_xpath(self.PRODUCT_IMAGES_CONTAINER)

    """Получает все стикеры с картинок продуктво на главной странице"""
    def get_all_stickers_from_product_images(self) -> None:
        images = self._get_all_products_images()
        for key, image in enumerate(images):
            try:
                # ToDo: Сейчас первый ключ для элемента меняется при кажом выхове словаря, нужно переделать
                self.stickers[key] = image.find_element_by_xpath(self.STICKER_CONTAINER).text
            except NoSuchElementException:
                continue

    """Проверка наличия стикеров"""
    def assert_stickers(self) -> None:
        assert self.stickers
        for product_number, product_sticker in self.stickers.items():
            print('product ' + str(product_number) + ' has sticker ' + product_sticker)
