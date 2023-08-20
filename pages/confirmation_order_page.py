from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_confirmation_locators import ConfirmationOrderPageLocators as l


class ConfirmationOrderPage:
    def __init__(self, driver):
        self.driver = driver

    def order_is_confirmed_popup(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(tuple(l.order_is_confirmes_popup)))
        return self.driver.find_element(*l.order_is_confirmes_popup).is_enabled()

    def see_status_bt(self):
        self.driver.find_element(*l.see_status_bt).click()
