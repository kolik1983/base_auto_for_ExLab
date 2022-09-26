import requests
import math
import sys
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Remote as RemoteWebDriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from .all_locators.locators_for_test_lending_page import BaseLocators
from colorama import init
from  colorama  import  Fore ,  Back ,  Style
import time

# Родительский класс
class BasePage():
    # Создаем конструкцию взаимодействия передачи ссылки в браузер
    def __init__(self, browser: RemoteWebDriver, url):
        self.browser = browser
        self.url = url


    # Создаем метод открытия и перехода по ссылке page.open()
    def open(self):
        self.browser.delete_all_cookies()  # Удоляем все куки
        self.browser.get(self.url)


    #  Если элемент найден, возвращаем True,
    #  иначе - перехватываем ошибку 'NoSuchElementException'
    #  и присваиваем False
    def is_element_present(self, how, what):
        try:
            WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((how, what)))
        except (NoSuchElementException):
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
