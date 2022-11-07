import requests
import math
import sys
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Remote as RemoteWebDriver, ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from .all_locators.locators_for_test_lending_page import BaseLocators
from colorama import init
from colorama import Fore, Style
import time

# Родительский класс
class BasePage():
    # Создаем конструкцию взаимодействия передачи ссылки в браузер
    def __init__(self, browser: RemoteWebDriver, url):
        self.browser = browser
        self.url = url

    # Создаем метод открытия и перехода по ссылке page.open()
    def open(self):
        self.browser.delete_all_cookies()  # Удаляем все куки
        self.browser.get(self.url)

    # def find(self, timeout=10):
    #     """ Find element on the page. """
    #     element = None
    #     try:
    #         element = WebDriverWait(self.browser, timeout).until(
    #            EC.presence_of_element_located(self.url)
    #         )
    #     except:
    #         print('Element not found on the page!')
    #     return element

    def is_element_present(self, how, what):
        try:
            WebDriverWait(self, 20).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_visible(self, how, what):
        try:
            WebDriverWait(self, 20).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_visible_elements(self, how, what):
        try:
            WebDriverWait(self, 20).until(EC.visibility_of_all_elements_located((how, what)))
        except TimeoutException:
            return False
        return True

    # Если элемент кликабельный, возвращаем True,
    # иначе - перехватываем ошибку 'NoSuchElementException'
    # и присваиваем False
    def is_element_clickable(self, how, what):
        try:
            WebDriverWait(self, 50).until(EC.element_to_be_clickable((how, what)))
        except (NoSuchElementException):
            return False
        return True

    def move_to_element(self, browser, how, what):
        try:
        # Переход до нужного элемента
            element = browser.find_element(how, what)
            actions = ActionChains(browser)
            actions.move_to_element(element).perform()
        except NoSuchElementException:
            return False
        return True


    def scroll_to_element(self, browser, how, what):
        try:
       # Скролл до элемента
            element = browser.find_element(how, what)
            browser.execute_script("arguments[0].scrollIntoView();", element)

        except NoSuchElementException:
            return False
        return True


    def scroll_down(self, browser):
        # ?Скролл вниз
        browser.execute_script("window.scrollTo(0,1000)")


    def get_current_url(self):
        # Возвращает текущий URL
        return self.browser.current_url

    def element_to_be_clickable(self, how, what):
        # Ожидает пока элемент не станет кликабельным
        try:
            WebDriverWait(self, 20).until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            return False
        return True


    def open_spoilers(self, browser, how, what):
        try:

            count_it = len(browser.find_elements(how, what))

            for area in range(1, count_it + 1):
                what_to_click = browser.find_element(how, f'({what})[{area}]')
                browser.execute_script('return arguments[0].scrollIntoView();', what_to_click)
                what_to_click.click()

        except NoSuchElementException:
            return False
        return True

    def scroll_to_futter(self, browser):

        try:
            browser.implicitly_wait(15)
            footer = browser.find_element(By.TAG_NAME, 'html')
            footer.send_keys(Keys.END)

        except NoSuchElementException:
            return False
        return True




