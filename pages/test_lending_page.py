
import pytest
import time
from lending.pages.all_locators.locators_for_test_lending_page import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class TestLandingPage():
    # Проверяем что страница лендинга загрузилась
    def test_open_my_page(self, browser):
        BasePage(browser, BaseLocators.LENDING_LINK).open()
        assert  BasePage.is_element_present(browser, *HeadersLendingPageLocators.HEADER_LENDING) is True, 'Лендинг не загрузился, логотип ExLab не отображается'
