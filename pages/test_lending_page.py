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


# class TestHeaders():
# @allure.feature('Page_test')
# @allure.story('Проверка загрузки страницы лендинга')
# #Проверяем что страница лендинга загрузилась
# def test_open_my_page(self, browser, open_url):
#     assert BasePage.is_element_present(browser, *HeadersLocators.HEADER_LENDING), 'Лендинг не загрузился, логотип ExLab не отображается'
#
# @allure.feature('Page_test')
# @allure.story('Проверка запуска темной темы')
# def test_open_black_theme(self, browser, open_url):
#     # Проверка что запущена темная тема, по переключателю который находится в положении включить светлую тему.
#     assert BasePage.is_element_present(browser, *HeadersLocators.SWITCH_LIGHT_THEME), 'Сейчас светла тема на сайте'
#
# @allure.feature('Logo_test')
# @allure.story('Проверка отображения логотипа ExLab')
# def test_logo_exlab(self, browser, open_url):
#     assert BasePage.is_visible(browser, *HeadersLocators.LOGO_PIC_EXLAB), 'Логотип отсутствует'
#
# @allure.feature('About_test')
# @allure.story('Проверка отображения пункта "О нас" в хедере')
# def test_link_about(self, browser,open_url):
#     assert BasePage.is_visible(browser, *HeadersLocators.HEADER_LINK_ABOUT), 'Пункт "О нас" отсутсвует'
#
# @allure.feature('About_test')
# @allure.story('Проверка кликабельности ссылки О нас')
# def test_about_us_click(self, browser, open_url):
#     assert BasePage.is_element_clickable(browser, *HeadersLocators.HEADER_LINK_ABOUT), 'Ссылка не кликабельна'
#
# @allure.feature('About_test')
# @allure.story('Проверка перехода по ссылке в пункт страницы О нас')
# def test_click_on_the_link_about(self, browser, open_url):
#     browser.find_element(*HeadersLocators.HEADER_LINK_ABOUT).click()
#     assert BasePage.is_visible(browser, *HeadersLocators.PARAGRAPH_ABOUT), 'Выбор элемента не ведет в соответсвующий пункт'
#
# @allure.feature('Project_test')
# @allure.story('Проверка отображения пункта "Проекты"')
# def test_link_project(self, browser, open_url):
#     assert BasePage.is_visible(browser, *HeadersLocators.HEADER_LINK_PROJECTS), 'Пункт "Проекты" отсутствует'
#
# @allure.feature('Project_test')
# @allure.story('Проверка кликабельности ссылки Проекты')
# def test_project_click(self, browser, open_url):
#     assert BasePage.is_element_clickable(browser, *HeadersLocators.HEADER_LINK_PROJECTS), 'Ссылка не кликабельна'
#
# @allure.feature('Project_test')
# @allure.story('Проверка перехода по ссылке в  пункт Проекты')
# def test_click_on_the_link_project(self, browser, open_url):
#     browser.find_element(*HeadersLocators.HEADER_LINK_PROJECTS).click()
#     # with allure.step('Делаем скрин'):
#     #     allure.attach(browser.get_full_page_screenshot_as_png(), name='Скрин', attachment_type=AttachmentType.PNG)
#     assert BasePage.is_visible(browser, *HeadersLocators.PARAGRAPH_PROJECT), 'Пункт "Проекты" отсутсвует'
#
# @allure.feature('Mentors_test')
# @allure.story('Проверка отображения пункта "Менторы"')
# def test_link_mentors(self, browser, open_url):
#     assert BasePage.is_visible(browser, *HeadersLocators.HEADER_LINK_MENTORS), 'ПУНКТ "Менторы" отсутсвует'
#
# @allure.feature('Mentors_test')
# @allure.story('Проверка кликабельности ссылки Менторы')
# def test_mentors_click(self, browser, open_url):
#     assert BasePage.is_element_clickable(browser, *HeadersLocators.HEADER_LINK_MENTORS), 'Ссылка не кликабельна'
#
# @allure.feature('Mentors_test')
# @allure.story('Проверка перехода в пункт Менторы')
# def test_click_on_the_link_mentors(self, browser, open_url):
#     browser.find_element(*HeadersLocators.HEADER_LINK_MENTORS).click()
#     assert BasePage.is_visible(browser, *HeadersLocators.PARAGRAPH_MENTORS), 'Переход в пункт  о менторах не осуществился'
#
# @allure.feature('Startup_test')
# @allure.story('Проверка отображения пункта "StartUp"')
# def test_link_startup(self, browser, open_url):
#     assert BasePage.is_visible(browser, *HeadersLocators.HEADER_LINK_STARTUP), 'Пункт "StartUp" отсутсвует'
#
# @allure.feature('Startup_test')
# @allure.story('Проверка кликабельности ссылки "StartUp"')
# def test_startup_click(self, browser, open_url):
#     assert BasePage.is_element_clickable(browser, *HeadersLocators.HEADER_LINK_STARTUP), 'Ссылка не кликабельна'
#
# @allure.feature('Startup_test')
# @allure.story('Проверка перехода в пункт "StartUp"')
# def test_click_on_the_link_startup(self, browser, open_url):
#     browser.find_element(*HeadersLocators.HEADER_LINK_STARTUP).click()
#     assert BasePage.is_visible(browser, *HeadersLocators.PARAGRAPH_STARTUP_FOR), 'Переход в пункт  "StartUp для" не осуществился'
#
# @allure.feature('Sun_icon_test')
# @allure.story('Проверка отображения Sun_icon')
# def test_visible_sunicon(self, browser, open_url):
#     assert BasePage.is_visible(browser,*HeadersLocators.SWITCH_LIGHT_THEME), 'Sun icon не отображается'
#
# @allure.feature('Sun_icon_test')
# @allure.story('Смены темы с темной на светлую')
# def test_change_to_white_theme(self, browser, open_url):
#     browser.find_element(*HeadersLocators.SWITCH_LIGHT_THEME).click()
#     assert BasePage.is_element_present(browser, *HeadersLocators.LIGHT_THEME), 'Нет перехода не светлую тему'

# @allure.feature('Join_button_test')
# @allure.story('Отображение кнопки "Присоединится" в хедере')
# def test_visible_button_join(self, browser, open_url):
#     assert BasePage.is_visible(browser, *HeadersLocators.JOIN_BUTTON), 'Кнопка "Присоединится" не отображается'
#
# @allure.feature('Join_button_test')
# @allure.story('Проверка кликабельности кнопки "Присоединится" в хедере')
# def test_clicable_but_join(self, browser, open_url):
#     assert BasePage.is_element_clickable(browser, *HeaderseLocators.JOIN_BUTTON), 'Кнопка "Присоединится" не кликабельна'
#
# @allure.feature('Join_button_test')
# @allure.story('Проверка перехода на страницу регистрации при нажатии на кнопку "Присоединится" в хедере')
# def test_click_join_button(self, browser, open_url):
#     browser.find_element(*HeadersLocators.JOIN_BUTTON).click()
#     browser.switch_to.window(browser.window_handles[1])
#     assert browser.current_url == BaseLocators.REGISTRATION_BOT, 'Переход на регистрацию не происходит'

# class TestPossibilityBlock():
#
#     @allure.feature('Possibility_block_tests')
#     @allure.story('Отображение логотипа  ExLab в блоке')
#     def test_logo_visible_in_block(self, browser, open_url):
#         assert BasePage.is_visible(browser, *PossibilityBlock.LOGO_EXLAB), 'Логотип в блоке "Твоя возможность" не отобразился'
#
#     @allure.feature('Possibility_block_tests')
#     @allure.story('Отображение надписи Твоя возможность')
#     def test_visible_title_possibility(self, browser, open_url):
#         assert BasePage.is_visible(browser, *PossibilityBlock.TITLE_POSSIBILITY), 'Нет заголовка "Твоя возможность"'
#
#     @allure.feature('Possibility_block_tests')
#     @allure.story('Отображение текста под надписью Твоя возможность')
#     def test_visible_text_undo_title(self, browser, open_url):
#         assert BasePage.is_visible(browser, *PossibilityBlock.TEXT_UNDO_TITLE), 'Текст под заголовком не виден'

# class TestAboutUsBlock():
    # @allure.feature('AboutUs_block_tests')
    # @allure.story('Отображение надписи О нас')
    # def test_visible_title_about_us(self, browser, open_url):
    #     # browser.find_element(*HeadersLocators.HEADER_LINK_ABOUT).click() # Другой способ протестировать, через клик
    #     BasePage.scroll_to_element(self, browser, *AboutUsBlock.TITLE_ABOUT)
    #     assert BasePage.is_visible(browser, *AboutUsBlock.TITLE_ABOUT), 'Нет заголовка "О нас"'
    #
    # @allure.feature('AboutUs_block_tests')
    # @allure.story('Отображение текста под надписью О нас')
    # def test_visibility_text_undo_title(self, browser, open_url):
    #     BasePage.scroll_to_element(self, browser, *AboutUsBlock.TEXT_UNDO_TITLE)
    #     assert BasePage.is_visible(browser, *AboutUsBlock.TEXT_UNDO_TITLE), 'Текст под заголовком О нас не виден'
    #
    # @allure.feature('AboutUs_block_tests')
    # @allure.story('Отображение надписи Почему ExLab?')
    # def test_visible_title_whyus(self,browser, open_url):
    #     BasePage.scroll_to_element(self, browser, *AboutUsBlock.TITLE_WHY)
    #     assert BasePage.is_visible(browser,*AboutUsBlock.TITLE_WHY), 'Нет заголова "Почему ExLab?"'

    # @allure.feature('AboutUs_block_tests')
    # @allure.story('Отображение текста под надписью Почему ExLab?')
    # def test_visibility_text_undo_whyus(self, browser, open_url):
    #     BasePage.scroll_to_element(self, browser, *AboutUsBlock.TEXT_UNDO_WHY)
    #     assert BasePage.is_visible(browser, *AboutUsBlock.TEXT_UNDO_WHY), 'Текст под заголовком "Почему ExLab?" не виден'
    #
    # @allure.feature('AboutUs_block_tests')
    # @allure.story('Отображение кнопки [Присоединиться]')
    # def test_visible_bnt_join(self, browser, open_url):
    #     BasePage.scroll_to_element(self, browser, *AboutUsBlock.TEXT_UNDO_WHY)
    #     assert BasePage.is_visible(browser, *AboutUsBlock.JOIN_BTN), 'Нет кнопки [Присоединиться]'
    #
    # @allure.feature('AboutUs_block_tests')
    # @allure.story('Кнопка [Присоединиться] кликабельна')
    # def test_btn_join_clickable(self, browser, open_url):
    #     BasePage.scroll_to_element(self, browser, *AboutUsBlock.TEXT_UNDO_WHY)
    #     assert BasePage.is_element_clickable(browser, *AboutUsBlock.JOIN_BTN), 'Не кликабельна [Присоединиться]'

    # @allure.feature('AboutUs_block_tests')
    # @allure.story('При нажатии на кнопку [Присоединиться] открывается форма регистрации')
    # def test_btn_join_clickable(self, browser, open_url):
    #     BasePage.scroll_to_element(self, browser, *AboutUsBlock.TEXT_UNDO_WHY)
    #     browser.find_element(*AboutUsBlock.JOIN_BTN).click()
    #     browser.switch_to.window(browser.window_handles[1])
    #     assert browser.current_url == BaseLocators.REGISTRATION_BOT
    #
# class TestProjectBlock():
#
#     @allure.feature('Project_block_tests')
#     @allure.story('Отображение заголовка Проекты')
#     def test_visible_title_project(self, browser, open_url):
#         BasePage.scroll_to_element(self, browser, *AllProjectBlock.TITLE_PROJECT)
#         assert BasePage.is_visible(browser, *AllProjectBlock.TITLE_PROJECT), 'Нет заголовка Проекты'
#
#     @allure.feature('Project_block_tests')
#     @allure.story('Отображение логотипов ExLab, HealthyLife, Easyhelp в блоке')
#     """тест методом параметаризации, выдает ошибку, не принимает values"""
#     @pytest.mark.parametrize(
#         "logo",
#         [*AllProjectBlock.PIC_EXLAB, *AllProjectBlock.PIC_HL, *AllProjectBlock.PIC_EH]
#         )
#     def test_visible_logo_all_projects(self, browser, open_url, logo):
#         BasePage.scroll_to_element(self, browser, logo)
#         assert BasePage.is_visible(browser, logo)
#
#     def test_visible_logo_all_projects(self, browser, open_url):
#         BasePage.scroll_to_element(self, browser, *AllProjectBlock.TITLE_PROJECT)
#         assert BasePage.is_visible(browser, *AllProjectBlock.THREE_LOGO)
#
#     @allure.feature('Project_block_tests')
#     @allure.story('Отображение текста под логотипами ExLab, HealthyLife, Easyhelp в блоке')
#     def test_visible_text_block_projects(self, browser, open_url):
#         BasePage.scroll_to_element(self, browser, *AllProjectBlock.TITLE_PROJECT)
#         assert BasePage.is_visible(browser, *AllProjectBlock.THREE_TEXT_BLOCK)

class TestMentorsBlock():
    # @allure.feature('Mentors_block_tests')
    # @allure.story('Отображение надписи Менторы')
    # def test_visible_title_mentors(self, browser, open_url):
    #     BasePage.scroll_to_element(self, browser, *MentorsBlock.TITLE_MENTORS)
    #     assert BasePage.is_visible(browser, *MentorsBlock.TITLE_MENTORS), 'Не отображается заголовок блока Менторы'
    #
    # @allure.feature('Mentors_block_tests')
    # @allure.story('Отображение надписи Менторы')
    # def test_open_area_mentor(self, browser, open_url):
    #     BasePage.scroll_to_element(self, browser, *MentorsBlock.AREA_MENTOR1)
    #     browser.find_element(*MentorsBlock.AREA_MENTOR1).click()
    #     assert BasePage.is_visible(browser, *MentorsBlock.SPOILER_MENTOR), 'Описание ментора не открылась'
    #
    # """пока не реализован нормальный локатор, before/after"""
    # """"@allure.feature('Mentors_block_tests')
    # @allure.story('- При нажатии на область ментора , знак "+" меняется на "-"')
    # def test_change_sing_in_area_mentor(self, browser, open_url):
    #     BasePage.scroll_to_element(self, browser, *MentorsBlock.AREA_MENTOR1)
    #     browser.find_element(*MentorsBlock.AREA_MENTOR1).click()"""
    #
    # @allure.feature('Mentors_block_tests')
    # @allure.story('При открытом спойлере фотография ментора отображается')
    # def test_visible_photo_mentor(self, browser, open_url):
    #     BasePage.scroll_to_element(self, browser, *MentorsBlock.AREA_MENTOR1)
    #     browser.find_element(*MentorsBlock.AREA_MENTOR1).click()
    #     assert BasePage.is_visible(browser, *MentorsBlock.PHOTOS_MENTORS), 'Фото менторов не отображается'
    #
    # @allure.feature('Mentors_block_tests')
    # @allure.story('При открытом спойлере отображается информации о менторе')
    # def test_visible_descriptions_mentor(self, browser, open_url):
    #     BasePage.scroll_to_element(self, browser, *MentorsBlock.AREA_MENTOR1)
    #     browser.find_element(*MentorsBlock.AREA_MENTOR1).click()
    #     assert BasePage.is_visible(browser, *MentorsBlock.DESCRIPTIONS_MENTORS), 'Описание менторов не видно'
    #
    # @allure.feature('Mentors_block_tests')
    # @allure.story('При нажатии на область ментора (при развернутом спойлере) спойлер закрывается')
    def test_close_spoiler(self, browser, open_url):
        BasePage.scroll_to_element(self, browser, *MentorsBlock.AREA_MENTOR1)
        browser.find_element(*MentorsBlock.AREA_MENTOR1).click()
        browser.find_element(*MentorsBlock.AREA_MENTOR1).click()
        assert BasePage.is_visible(browser, *MentorsBlock.CLOSE_AREA)

    # @allure.feature('Mentors_block_tests')НЕТ ЛОКАТОРА 3 теста минус
    # @allure.story('Отображение  кнопки [Стать ментором]')
    # def test_visible_become_ment_btn(self, browser, open_url):
    #     BasePage.scroll_to_element(self, browser, )

# class TestStartUpBlock():
#
#     @allure.feature('Startup_block_tests')
#     @allure.story('Отображение надписи StartUp для ')
#     def test_visible_startup_title(self, browser, open_url):
#         BasePage.scroll_to_element(self, browser, *StartUpBlock.TITLE_STARTUP)
#         assert BasePage.is_visible(browser, *StartUpBlock.TITLE_STARTUP), 'Не видно заголовок блока StartUp'



































