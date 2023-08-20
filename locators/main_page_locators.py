from selenium.webdriver.common.by import By


class MainPageLocators:
    questions_block = [By.CSS_SELECTOR, ".Home_FAQ__3uVm4"]
    answer = [By.XPATH, ".//div[@id='accordion__panel-0']/p"]
    order_bt_upper = [By.CSS_SELECTOR, 'div.Header_Nav__AGCXC button.Button_Button__ra12g']
    order_bt_lower = [By.CSS_SELECTOR, 'button.Button_Middle__1CSJM']
