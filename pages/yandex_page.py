from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.yandex_page_locators import YaPageLocators as l
from selenium.webdriver.common.by import By


class YaPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_search_bt(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(tuple(l.search_bt)))

