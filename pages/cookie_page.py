from locators.cookie_page_locators import CookiePageLocators as l


class CookiePage:
    def __init__(self, driver):
        self.driver = driver

    def click_agree_cookie(self):
        self.driver.find_element(*l.cookie_bt).click()

