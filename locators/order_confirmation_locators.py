from selenium.webdriver.common.by import By


class ConfirmationOrderPageLocators:
    order_is_confirmes_popup = [By.CSS_SELECTOR, '.Order_Modal__YZ-d3']
    see_status_bt = [By.XPATH, ".//button[text()='Посмотреть статус']"]