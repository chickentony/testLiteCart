from selenium.common.exceptions import NoSuchElementException


class ProductPage:
    def __init__(self, driver):
        # Инициализация браузера
        self.driver = driver
        # Заголовок товара
        self.PRODUCT_HEADER: str = '//div[@id="box-product"]//h1'
        # Контейнер с ценой товара
        self.REGULAR_PRICE_CONTAINER: str = '//div[@class="price-wrapper"]/s[@class="regular-price"]'
        # Контейнер со специальной(акционной, скидочной) ценой товара
        self.CAMPAIGN_PRICE_CONTAINER: str = '//div[@class="price-wrapper"]/strong[@class="campaign-price"]'
        # Название товара
        self.product_name: str = ''
        # Цена товара
        self.product_regular_price: str = ''
        # Акционная цена товара
        self.sale_price: str = ''
        # Словарь со стилями цены товара
        self.product_regular_price_styles: dict = {}
        # Словарь со стилями скиодчной цены товара
        self.product_sale_price_styles: dict = {}
        # ToDo: надо ли?
        self.not_found_element = False

    # Получает название и цены продукта
    def get_product_name_and_prices(self) -> None:
        self.product_name = self.driver.find_element_by_xpath(self.PRODUCT_HEADER).text
        self.product_regular_price = self.driver.find_element_by_xpath(self.REGULAR_PRICE_CONTAINER).text
        try:
            self.sale_price = self.driver.find_element_by_xpath(self.CAMPAIGN_PRICE_CONTAINER).text
        except NoSuchElementException:
            self.sale_price = 'Product has no sale'

    # Получает стиили продукта
    def get_product_prices_styles(self) -> None:
        self.product_regular_price_styles['color'] = \
            self.driver.find_element_by_xpath(self.REGULAR_PRICE_CONTAINER).value_of_css_property('color')
        self.product_regular_price_styles['text-decoration'] = \
            self.driver.find_element_by_xpath(self.REGULAR_PRICE_CONTAINER).value_of_css_property('text-decoration')
        self.product_regular_price_styles['font-size'] = \
            self.driver.find_element_by_xpath(self.REGULAR_PRICE_CONTAINER).value_of_css_property('font-size')
        try:
            self.product_sale_price_styles['color'] = \
                self.driver.find_element_by_xpath(self.CAMPAIGN_PRICE_CONTAINER).value_of_css_property('color')
            self.product_sale_price_styles['text-decoration'] = \
                self.driver.find_element_by_xpath(self.CAMPAIGN_PRICE_CONTAINER).value_of_css_property(
                    'text-decoration')
            self.product_sale_price_styles['font-size'] = \
                self.driver.find_element_by_xpath(self.CAMPAIGN_PRICE_CONTAINER).value_of_css_property('font-size')
        except NoSuchElementException:
            self.not_found_element = True
