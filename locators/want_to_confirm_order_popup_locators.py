from selenium.webdriver.common.by import By


class ConfirmOrderPageLocators:
    popup = [By.CSS_SELECTOR, '.Order_ModalHeader__3FDaJ']
    yes_bt = [By.XPATH, ".//button[text()='Да']"]