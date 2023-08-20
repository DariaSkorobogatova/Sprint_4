from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators as l
from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_main_page(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_main_page_to_load(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(tuple(l.order_bt_upper)))

    def wait_for_question_block_to_load(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(tuple(l.questions_block)))

    def scroll_to_question_block(self, id):
        question_block = self.driver.find_element(By.ID, f"accordion__heading-{id}")
        self.driver.execute_script("arguments[0].scrollIntoView();", question_block)

    def click_question(self, id):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.ID, f"accordion__heading-{id}")))
        self.driver.find_element(By.ID, f"accordion__heading-{id}").click()

    def return_answer_text(self, id):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.ID, f"accordion__panel-{id}")))
        return self.driver.find_element(By.XPATH, f".//div[@id='accordion__panel-{id}']/p").text

    def click_order_bt(self):
        self.driver.find_element(*l.order_bt_upper).click()



