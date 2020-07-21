from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()
        self.PRODUCT_HEADER: str = '//div[@id="box-product"]//h1'
        self.REGULAR_PRICE_CONTAINER: str = '//div[@class="price-wrapper"]/s[@class="regular-price"]'
        self.CAMPAIGN_PRICE_CONTAINER: str = '//div[@class="price-wrapper"]/strong[@class="campaign-price"]'
        self.product_name: str = ''
        self.product_regular_price: str = ''
        self.sale_price: str = ''
        self.product_regular_price_styles: dict = {}
        self.product_sale_price_styles: dict = {}

    def get_product_name_and_prices(self):
        self.product_name = self.driver.find_element_by_xpath(self.PRODUCT_HEADER).text
        self.product_regular_price = self.driver.find_element_by_xpath(self.REGULAR_PRICE_CONTAINER).text
        try:
            self.sale_price = self.driver.find_element_by_xpath(self.CAMPAIGN_PRICE_CONTAINER).text
        except NoSuchElementException:
            self.sale_price = 'Product has no sale'

    def get_product_prices_styles(self):
        self.product_regular_price_styles['color'] = \
            self.driver.find_element_by_xpath(self.REGULAR_PRICE_CONTAINER).value_of_css_property('color')
        self.product_regular_price_styles['text-decoration'] = \
            self.driver.find_element_by_xpath(self.REGULAR_PRICE_CONTAINER).value_of_css_property('text-decoration')
        self.product_regular_price_styles['font-size'] = \
            self.driver.find_element_by_xpath(self.REGULAR_PRICE_CONTAINER).value_of_css_property('font-size')
        print(self.product_regular_price_styles)
        # Проверить наличие
        self.product_sale_price_styles['color'] = \
            self.driver.find_element_by_xpath(self.CAMPAIGN_PRICE_CONTAINER).value_of_css_property('color')
        self.product_sale_price_styles['text-decoration'] = \
            self.driver.find_element_by_xpath(self.CAMPAIGN_PRICE_CONTAINER).value_of_css_property('text-decoration')
        self.product_sale_price_styles['font-size'] = \
            self.driver.find_element_by_xpath(self.CAMPAIGN_PRICE_CONTAINER).value_of_css_property('font-size')
        print(self.product_sale_price_styles)

    def assert_product_name_and_price(
            self,
            expected_product_name: str,
            expected_regular_price: str,
            expected_sale_price=None
    ):
        if expected_regular_price == self.product_regular_price and expected_product_name == self.product_name:
            print('Product name and regular price are same')
        elif expected_sale_price and expected_sale_price == self.sale_price:
            print('Sale price are same')
        else:
            raise AssertionError('Check')
