import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Подождать кликабельность элемента')
    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step('Кликнуть по элементу')
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Получить текст элемента')
    def get_answer(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Ввод текста')
    def send_keys(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Нажатие ESC')
    def click_escape(self):
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)

    @allure.step('Дождаться отображения текста')
    def wait_for_text(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator)).text

    @allure.step('Переход на другую вкладку')
    def switch_new_tab(self, url):
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(EC.url_to_be(url))

    @allure.step('Получить URL')
    def get_current_url(self):
        return self.driver.current_url
