
from selenium import webdriver


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()
        self.PRODUCT_HEADER: str = '//div[@id="box-product"]//h1'

    def get_product_name_and_price(self):
        product_name = self.driver.find_element_by_xpath(self.PRODUCT_HEADER).text
        print(product_name)