
# Тут возможно стоит пересмотреть и некоторые убрать, наверно они все не нужны, достаточно базовых методов. где та грань

import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Подождать кликабельность кнопки Заказать вверху страницы')
    def wait_for_clickable_order_button_in_header(self):
            self.wait_for_clickable(MainPageLocators.ORDER_BUTTON_IN_HEADER)

    @allure.step('Кликнуть по кнопке Заказать вверху страницы')
    def click_order_button_in_header(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_IN_HEADER)

    @allure.step('Подождать кликабельность кнопки Заказать внизу страницы')
    def wait_for_clickable_order_button_in_main(self):
            self.wait_for_clickable(MainPageLocators.ORDER_BUTTON_IN_MAIN)

    @allure.step('Переход к кнопке Заказать внизу страницы')
    def scroll_to_order_button_in_main(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_IN_MAIN)

    @allure.step('Кликнуть по кнопке Заказать внизу страницы')
    def click_order_button_in_main(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_IN_MAIN)

    @allure.step('Подождать прогрузки лого Самокат')
    def wait_for_clickable_scooter_logo(self):
        self.wait_for_clickable(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Кликнуть по лого Самокат')
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Подождать прогрузки лого Яндекс')
    def wait_for_clickable_yandex_logo(self):
        self.wait_for_clickable(MainPageLocators.YANDEX_LOGO)

    @allure.step('Кликнуть по лого Яндекс')
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    @allure.step('Переход к списку вопросов')
    def scroll_to_questions_place(self):
        self.scroll_to_element(MainPageLocators.QUESTIONS_TITLE)

    @allure.step('Кликнуть на вопрос по индексу')
    def click_question(self, index):
        self.scroll_to_element(MainPageLocators.QUESTIONS[index])
        self.click_element(MainPageLocators.QUESTIONS[index])

    @allure.step('Получить ответ по индексу')
    def get_answer_text(self, index):
        return self.get_answer(MainPageLocators.ANSWERS[index])

    @allure.step('Кликнуть по кнопке Да все уже привыкли')
    def click_cookie_button(self):
        self.click_element(MainPageLocators.COOKIE_BUTTON)


