import pytest
import allure

from pages.main_page import MainPage
from data import TestData, Urls


class TestQuestions:

    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description('Кликнуть на стрелку, дожидаться появления ответа на вопрос. Проверка текста ответа.')
    @pytest.mark.parametrize("question_index", [0, 1, 2, 3, 4, 5, 6, 7])
    def test_click_faq_questions(self, driver, question_index):
        main_page = MainPage(driver)
        main_page.click_cookie_button()
        main_page.scroll_to_questions_place()
        main_page.click_question(question_index)
        answer_text = main_page.get_answer_text(question_index)

        assert answer_text == TestData.ANSWER_TEXTS[question_index]

class Testlogo:

    @allure.title('Проверка перехода на страницу "Дзена" при клике на логотип "Яндекс"')
    @allure.description('Нажать на лого Яндекс и переходим в новую открывшуюся вкладку. Проверяем, что url соответствует адресу страницы Дзен')
    def test_click_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_clickable_yandex_logo()
        main_page.click_yandex_logo()
        main_page.switch_new_tab(Urls.YANDEX_LOGO_URL)
        current_url = main_page.get_current_url()
        expected_url = Urls.DZEN_URL
        assert expected_url in current_url


    @allure.title('Проверка перехода на главную страницу сервиса при клике на логотип Самокат')
    @allure.description('Перейти на страницу заказа, кликнуть по лого Самоката. Проверка, что url соответствует главной странице Самоката')
    def test_click_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_clickable_scooter_logo()
        main_page.click_order_button_in_header()
        main_page.click_scooter_logo()
        current_url = main_page.get_current_url()
        expected_url = Urls.MAIN_URL
        assert expected_url in current_url
