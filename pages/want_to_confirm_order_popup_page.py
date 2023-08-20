from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.want_to_confirm_order_popup_locators import ConfirmOrderPageLocators as l
from selenium.webdriver.common.by import By


class ConfirmOrderPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_popup(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(tuple(l.popup)))

    def click_yes_bt(self):
        self.driver.find_element(*l.yes_bt).click()
