from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class UiHelper:

    # Инициализация драйвера
    def __init__(self, driver) -> None:
        self.webdriver = driver

    # Ожидание загрузки страницы
    def wait_till_page_load(self, locator_xpath: str) -> WebDriverWait:
        wait = WebDriverWait(self.webdriver, 10)
        return wait.until(EC.presence_of_element_located((By.XPATH, locator_xpath)))

    @staticmethod
    def assert_true(condition: bool):
        if condition:
            return True
        raise Exception('Condition is not true')
