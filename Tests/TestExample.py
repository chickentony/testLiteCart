from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

wb = webdriver.Chrome()
wb.get('https://google.com')
wb.find_element_by_xpath('//input[@class="gLFyf gsfi"]').send_keys('Wikipedia')
wb.find_element_by_xpath('//input[@class="gLFyf gsfi"]').send_keys(Keys.ENTER)
WebDriverWait(wb, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@class="logo"]')))
wb.quit()
