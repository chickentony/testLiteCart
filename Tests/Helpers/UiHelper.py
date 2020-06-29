# from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class UiHelper:

    def __init__(self, driver):
        self.webdriver = driver

    def wait_till_page_load(self, locator_xpath: str):
        wait = WebDriverWait(self.webdriver, 10)
        return wait.until(EC.presence_of_element_located((By.XPATH, locator_xpath)))
