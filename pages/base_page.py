import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    timeout = 5

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Перейти на страницу')
    def go_to_page(self, url):
        self.driver.get(url)

    @allure.step('Вернуть url страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Дождаться загрузки')
    def wait_for_loading(self, locator):
        WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Проскроллить страницу до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Кликнуть по элементу')
    def click_element(self, locator):
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator)).click()

    @allure.step('Вернуть текст элемента')
    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
        return element.text

    @allure.step('Ввести данные в поле ввода')
    def input_data(self, locator, data):
        WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
        self.driver.find_element(*locator).send_keys(data)

    @allure.step('Проверить, что кнопка активна')
    def element_is_enabled(self, locator):
        WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator).is_enabled()

    @allure.step('Переключиться на вторую вкладку браузера')
    def switch_to_second_tab(self):
        WebDriverWait(self.driver, self.timeout).until_not(EC.number_of_windows_to_be(1))
        second_tab = self.driver.window_handles[1]
        self.driver.switch_to.window(second_tab)

