import time
from .base_page import BasePage
from lending.pages.all_locators.locators_for_test_lending_page import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait



class TestLandingPage():
    def test_open_my_page(self, browser):
        BasePage(browser, BaseLocators.LENDING_LINK).open()


        status_logo_exlab = BasePage.is_element_present(self, *HeadersLendingPageLocators.HEADER_LENDING)
        print(status_logo_exlab)
        assert status_logo_exlab == True, 'Перехода на страницу лендинка не произошло'
