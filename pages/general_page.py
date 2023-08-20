from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.general_page_locators import GeneralPageLocators as l


class GeneralPage:
    def __init__(self, driver):
        self.driver = driver

    def click_scooter_logo(self):
        self.driver.find_element(*l.scooter_logo).click()

    def click_yandex_logo(self):
        self.driver.find_element(*l.yandex_logo).click()

    def windows_switch(self):
        WebDriverWait(self.driver, 3).until(EC.number_of_windows_to_be(2))
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)