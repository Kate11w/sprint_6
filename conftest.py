import pytest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from data import Urls

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.get(Urls.MAIN_URL)
    yield driver
    driver.quit()