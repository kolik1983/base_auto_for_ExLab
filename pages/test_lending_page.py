import pytest
import time
import allure
from allure_commons.types import AttachmentType
import webbrowser
from pages.all_locators.locators_for_test_lending_page import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class TestLanding():
    #Проверяем что страница лендинга загрузилась
    def test_open_my_page(self, browser, open_url):
        assert BasePage.is_element_present(browser, *HeadersLendingPageLocators.HEADER_LENDING), 'Лендинг не загрузился, логотип ExLab не отображается'

    def test_open_black_theme(self, browser, open_url):
        # Проверка что запущена темная тема, по переключателю который находится в положении включить светлую тему.
        assert BasePage.is_element_present(browser, *HeadersLendingPageLocators.SWITCH_WHITE_THEME), 'Сейчас светла тема на сайте'

    def test_logo_exlab(self, browser, open_url):
        # Проверка отображения логотипа ExLab
        assert BasePage.is_visible(browser, *HeadersLendingPageLocators.LOGO_PIC_EXLAB), 'Логотип отсутсвует'

    def test_link_about(self, browser,open_url):
        # Проверка отображения пункта "О нас" в хедере
        assert BasePage.is_visible(browser, *HeadersLendingPageLocators.HEADER_LINK_ABOUT), 'Пункт "О нас" отсутсвует'

    def test_about_us_click(self, browser, open_url):
        # Проверка кликабельности ссылки О нас
        assert BasePage.is_element_clickable(browser, *HeadersLendingPageLocators.HEADER_LINK_ABOUT), 'Ссылка не кликабельна'

    def test_click_on_the_link_about(self, browser, open_url):
        # Проверка перехода по ссылке в пункт страницы О нас
        browser.find_element(*HeadersLendingPageLocators.HEADER_LINK_ABOUT).click()
        assert BasePage.is_visible(browser, *HeadersLendingPageLocators.PARAGRAPH_ABOUT), 'Выбор элемента не ведет в соответсвующий пункт'

    @allure.feature('Project_test')
    @allure.story('Проверка отображения пункта "Проекты"')
    def test_link_project(self, browser, open_url):
        # Проверка отображения пункта "Проекты"
        assert BasePage.is_visible(browser, *HeadersLendingPageLocators.HEADER_LINK_PROJECTS), 'Пункт "Проекты" отсутствует'

    @allure.feature('Project_test')
    @allure.story('Проверка кликабельности ссылки Проекты')
    def test_project_click(self, browser, open_url):
        # Проверка кликабельности ссылки Проекты
        assert BasePage.is_element_clickable(browser, *HeadersLendingPageLocators.HEADER_LINK_PROJECTS), 'Ссылка не кликабельна'

    @allure.feature('Project_test')
    @allure.story('Проверка перехода по ссылке в соответсвующий пункт')
    def test_click_on_the_link_project(self, browser, open_url):
        # Проверка перехода по ссылке в соответсвующий пункт
        # allure.attach(browser.get_full_page_screenshot_as_png(), name='Скрин', attachment_type=AttachmentType.PNG)
        browser.find_element(*HeadersLendingPageLocators.HEADER_LINK_PROJECTS).click()
        assert BasePage.is_visible(browser, *HeadersLendingPageLocators.PARAGRAPH_PROJECT), 'Пункт "Проекты" отсутсвует'

    def test_link_mentors(self, browser, open_url):
        # Проверка отображения пункта "Менторы"
        assert BasePage.is_visible(browser, *HeadersLendingPageLocators.HEADER_LINK_MENTORS), 'ПУНКТ "Менторы" отсутсвует'

    def test_mentors_click(self, browser, open_url):
        # Проверка кликабельности ссылки Менторы
        assert BasePage.is_element_clickable(browser, *HeadersLendingPageLocators.HEADER_LINK_MENTORS), 'Ссылка не кликабельна'

    def test_click_on_the_link_mentors(self, browser, open_url):
        # Проверка перехода в пункт Менторы
        browser.find_element(*HeadersLendingPageLocators.HEADER_LINK_MENTORS).click()
        assert BasePage.is_visible(browser, *HeadersLendingPageLocators.PARAGRAPH_MENTORS), 'Переход в пункт  о менторах не осуществился'



