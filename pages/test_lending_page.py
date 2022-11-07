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



class TestHeaders():

    @allure.feature('Page_test')
    @allure.story('Проверка загрузки страницы лендинга')
    #Проверяем что страница лендинга загрузилась
    def test_open_my_page(self, browser, open_url):
        assert BasePage.is_element_present(browser, *HeadersLocators.HEADER_LENDING), 'Лендинг не загрузился, логотип ExLab не отображается'

    @allure.feature('Page_test')
    @allure.story('Проверка запуска темной темы')
    def test_open_black_theme(self, browser, open_url):
    # Проверка, что запущена темная тема, по переключателю который находится в положении включить светлую тему.
        assert BasePage.is_element_present(browser, *HeadersLocators.SWITCH_LIGHT_THEME), 'Сейчас светла тема на сайте'

    @allure.feature('Logo_test')
    @allure.story('Проверка отображения логотипа ExLab')
    def test_logo_exlab(self, browser, open_url):
        assert BasePage.is_visible(browser, *HeadersLocators.LOGO_PIC_EXLAB), 'Логотип отсутствует'

    @allure.feature('About_test')
    @allure.story('Проверка отображения пункта "О нас" в хедере')
    def test_link_about(self, browser,open_url):
        assert BasePage.is_visible(browser, *HeadersLocators.HEADER_LINK_ABOUT), 'Пункт "О нас" отсутствует'

    @allure.feature('About_test')
    @allure.story('Проверка перехода по ссылке в пункт страницы О нас')
    def test_click_on_the_link_about(self, browser, open_url):
        browser.find_element(*HeadersLocators.HEADER_LINK_ABOUT).click()
        assert BasePage.is_visible(browser, *HeadersLocators.PARAGRAPH_ABOUT), 'Выбор элемента не ведет в соответсвующий пункт'

    @allure.feature('Project_test')
    @allure.story('Проверка отображения пункта "Проекты"')
    def test_link_project(self, browser, open_url):
        assert BasePage.is_visible(browser, *HeadersLocators.HEADER_LINK_PROJECTS), 'Пункт "Проекты" отсутствует'

    @allure.feature('Project_test')
    @allure.story('Проверка перехода по ссылке в  пункт Проекты')
    def test_click_on_the_link_project(self, browser, open_url):
        browser.find_element(*HeadersLocators.HEADER_LINK_PROJECTS).click()
        # with allure.step('Делаем скрин'):
        #     allure.attach(browser.get_full_page_screenshot_as_png(), name='Скрин', attachment_type=AttachmentType.PNG)
        assert BasePage.is_visible(browser, *HeadersLocators.PARAGRAPH_PROJECT), 'Пункт "Проекты" отсутствует'

    @allure.feature('Mentors_test')
    @allure.story('Проверка отображения пункта "Менторы"')
    def test_link_mentors(self, browser, open_url):
        assert BasePage.is_visible(browser, *HeadersLocators.HEADER_LINK_MENTORS), 'ПУНКТ "Менторы" отсутствует'

    @allure.feature('Mentors_test')
    @allure.story('Проверка перехода в пункт Менторы')
    def test_click_on_the_link_mentors(self, browser, open_url):
        browser.find_element(*HeadersLocators.HEADER_LINK_MENTORS).click()
        assert BasePage.is_visible(browser, *HeadersLocators.PARAGRAPH_MENTORS), 'Переход в пункт  о менторах не осуществился'

    @allure.feature('Startup_test')
    @allure.story('Проверка отображения пункта "StartUp"')
    def test_link_startup(self, browser, open_url):
        assert BasePage.is_visible(browser, *HeadersLocators.HEADER_LINK_STARTUP), 'Пункт "StartUp" отсутствует'

    @allure.feature('Startup_test')
    @allure.story('Проверка перехода в пункт "StartUp"')
    def test_click_on_the_link_startup(self, browser, open_url):
        browser.find_element(*HeadersLocators.HEADER_LINK_STARTUP).click()
        assert BasePage.is_visible(browser, *HeadersLocators.PARAGRAPH_STARTUP_FOR), 'Переход в пункт  "StartUp для" не осуществился'

    @allure.feature('Sun_icon_test')
    @allure.story('Проверка отображения Sun_icon')
    def test_visible_sun_icon(self, browser, open_url):
        assert BasePage.is_visible(browser,*HeadersLocators.SWITCH_LIGHT_THEME), 'Sun icon не отображается'

    @allure.feature('Sun_icon_test')
    @allure.story('Смены темы с темной на светлую')
    def test_change_to_white_theme(self, browser, open_url):
        browser.find_element(*HeadersLocators.SWITCH_LIGHT_THEME).click()
        assert BasePage.is_element_present(browser, *HeadersLocators.LIGHT_THEME), 'Нет перехода не светлую тему'

    @allure.feature('Join_button_test')
    @allure.story('Отображение кнопки "Присоединится" в хедере')
    def test_visible_button_join(self, browser, open_url):
        assert BasePage.is_visible(browser, *HeadersLocators.JOIN_BUTTON), 'Кнопка "Присоединится" не отображается'

    @allure.feature('Join_button_test')
    @allure.story('Проверка перехода на страницу регистрации при нажатии на кнопку "Присоединится" в хедере')
    def test_click_join_button(self, browser, open_url):
        browser.find_element(*HeadersLocators.JOIN_BUTTON).click()
        browser.switch_to.window(browser.window_handles[1])
        assert browser.current_url == BaseLocators.REGISTRATION_BOT, 'Переход на регистрацию не происходит'

class TestPossibilityBlock():

    @allure.feature('Possibility_block_tests')
    @allure.story('Отображение логотипа  ExLab в блоке')
    def test_logo_visible_in_block(self, browser, open_url):
        assert BasePage.is_visible(browser, *PossibilityBlock.LOGO_EXLAB), 'Логотип в блоке "Твоя возможность" не отобразился'

    @allure.feature('Possibility_block_tests')
    @allure.story('Отображение надписи Твоя возможность')
    def test_visible_title_possibility(self, browser, open_url):
        assert BasePage.is_visible(browser, *PossibilityBlock.TITLE_POSSIBILITY), 'Нет заголовка "Твоя возможность"'

    @allure.feature('Possibility_block_tests')
    @allure.story('Отображение текста под надписью Твоя возможность')
    def test_visible_text_undo_title(self, browser, open_url):
        assert BasePage.is_visible(browser, *PossibilityBlock.TEXT_UNDO_TITLE), 'Текст под заголовком не виден'

class TestAboutUsBlock():

    @allure.feature('AboutUs_block_tests')
    @allure.story('Отображение надписи О нас')
    def test_visible_title_about_us(self, browser, open_url):
        # browser.find_element(*HeadersLocators.HEADER_LINK_ABOUT).click() # Другой способ протестировать, через клик
        BasePage.scroll_to_element(self, browser, *AboutUsBlock.TITLE_ABOUT)
        assert BasePage.is_visible(browser, *AboutUsBlock.TITLE_ABOUT), 'Нет заголовка "О нас"'

    @allure.feature('AboutUs_block_tests')
    @allure.story('Отображение текста под надписью О нас')
    def test_visibility_text_undo_title(self, browser, open_url):
        BasePage.scroll_to_element(self, browser, *AboutUsBlock.TEXT_UNDO_TITLE)
        assert BasePage.is_visible(browser, *AboutUsBlock.TEXT_UNDO_TITLE), 'Текст под заголовком О нас не виден'

    @allure.feature('AboutUs_block_tests')
    @allure.story('Отображение надписи Почему ExLab?')
    def test_visible_title_whyus(self,browser, open_url):
        BasePage.scroll_to_element(self, browser, *AboutUsBlock.TITLE_WHY)
        assert BasePage.is_visible(browser,*AboutUsBlock.TITLE_WHY), 'Нет заголова "Почему ExLab?"'

    @allure.feature('AboutUs_block_tests')
    @allure.story('Отображение текста под надписью Почему ExLab?')
    def test_visibility_text_undo_whyus(self, browser, open_url):
        BasePage.scroll_to_element(self, browser, *AboutUsBlock.TEXT_UNDO_WHY)
        assert BasePage.is_visible(browser, *AboutUsBlock.TEXT_UNDO_WHY), 'Текст под заголовком "Почему ExLab?" не виден'

    @allure.feature('AboutUs_block_tests')
    @allure.story('Отображение кнопки [Присоединиться]')
    def test_visible_bnt_join(self, browser, open_url):
        BasePage.scroll_to_element(self, browser, *AboutUsBlock.TEXT_UNDO_WHY)
        assert BasePage.is_visible(browser, *AboutUsBlock.JOIN_BTN), 'Нет кнопки [Присоединиться]'

    @allure.feature('AboutUs_block_tests')
    @allure.story('При нажатии на кнопку [Присоединиться] открывается форма регистрации')
    def test_btn_join_click(self, browser, open_url):
        BasePage.scroll_to_element(self, browser, *AboutUsBlock.TEXT_UNDO_WHY)
        browser.find_element(*AboutUsBlock.JOIN_BTN).click()
        browser.switch_to.window(browser.window_handles[1])
        assert browser.current_url == BaseLocators.REGISTRATION_BOT

class TestProjectBlock():

    @allure.feature('Project_block_tests')
    @allure.story('Отображение заголовка Проекты')
    def test_visible_title_project(self, browser, open_url):
        BasePage.scroll_to_element(self, browser, *AllProjectBlock.TITLE_PROJECT)
        assert BasePage.is_visible(browser, *AllProjectBlock.TITLE_PROJECT), 'Нет заголовка Проекты'

    # @allure.feature('Project_block_tests')
    # @allure.story('Отображение логотипов ExLab, HealthyLife, Easyhelp в блоке')
    # @pytest.mark.parametrize(
    #     "logo",
    #     [*AllProjectBlock.PIC_EXLAB, *AllProjectBlock.PIC_HL, *AllProjectBlock.PIC_EH]
    #     )
    # def test_visible_logo_all_projects(self, browser, open_url, logo):
    #     BasePage.scroll_to_element(self, browser, logo)
    #     assert BasePage.is_visible(browser, logo)

    def test_visible_logo_all_projects(self, browser, open_url):
        BasePage.scroll_to_element(self, browser, *AllProjectBlock.TITLE_PROJECT)
        assert BasePage.is_visible(browser, *AllProjectBlock.THREE_LOGO)

    @allure.feature('Project_block_tests')
    @allure.story('Отображение текста под логотипами ExLab, HealthyLife, Easyhelp в блоке')
    def test_visible_text_block_projects(self, browser, open_url):
        BasePage.scroll_to_element(self, browser, *AllProjectBlock.TITLE_PROJECT)
        assert BasePage.is_visible(browser, *AllProjectBlock.THREE_TEXT_BLOCK)

class TestMentorsBlock():
    @allure.feature('Mentors_block_tests')
    @allure.story('Отображение надписи Менторы')
    def test_visible_title_mentors(self, browser, open_url):
        BasePage.scroll_to_element(self, browser, *MentorsBlock.TITLE_MENTORS)
        assert BasePage.is_visible(browser, *MentorsBlock.TITLE_MENTORS), 'Не отображается заголовок блока Менторы'

    @allure.feature('Mentors_block_tests')
    @allure.story('При нажатии на область ментора , открывается спойлер')
    def test_open_area_mentor(self, browser, open_url):
        browser.implicitly_wait(2)
        BasePage.scroll_to_element(self, browser, *HeadersLocators.PARAGRAPH_MENTORS)
        BasePage.open_spoilers(self, browser, *MentorsBlock.TITLE_MENTORS)
        assert len(browser.find_elements(*MentorsBlock.SPOILERS_MENTOR)) == 4, "Не все спойлеры открылись"

    @allure.feature('Mentors_block_tests')
    @allure.story('При открытом спойлере фотография ментора отображается')
    def test_visible_photo_mentor(self, browser, open_url):
        browser.implicitly_wait(2)
        BasePage.scroll_to_element(self, browser, *HeadersLocators.PARAGRAPH_MENTORS)
        BasePage.open_spoilers(self, browser, *MentorsBlock.TITLE_MENTORS)
        assert len(browser.find_elements(*MentorsBlock.PHOTOS_MENTORS)) == 4, 'Не все фото менторов не отображаются'

    @allure.feature('Mentors_block_tests')
    @allure.story('При открытом спойлере отображается информации о менторе')
    def test_visible_descriptions_mentor(self, browser, open_url):
        browser.implicitly_wait(2)
        BasePage.scroll_to_element(self, browser, *HeadersLocators.PARAGRAPH_MENTORS)
        BasePage.open_spoilers(self, browser, *MentorsBlock.TITLE_MENTORS)
        assert len(browser.find_elements(*MentorsBlock.DESCRIPTIONS_MENTORS)) == 4, 'Описание не всех менторов видно'

    @allure.feature('Mentors_block_tests')
    @allure.story('При нажатии на область ментора (при развернутом спойлере) спойлер закрывается')
    def test_close_spoiler(self, browser, open_url):
        browser.implicitly_wait(2)
        BasePage.scroll_to_element(self, browser, *HeadersLocators.PARAGRAPH_MENTORS)
        BasePage.open_spoilers(self, browser, *MentorsBlock.TITLE_MENTORS)
        BasePage.open_spoilers(self, browser, *MentorsBlock.TITLE_MENTORS)
        assert len(browser.find_elements(*MentorsBlock.SPOILERS_MENTOR)) == 0, "Не все спойлеры закрылись"

class TestStartUpBlock():

    @allure.feature('Startup_block_tests')
    @allure.story('Отображение надписи StartUp')
    def test_visible_startup_title(self, browser, open_url):
        BasePage.scroll_to_element(self, browser, *StartUpBlock.TITLE_STARTUP)
        assert BasePage.is_visible(browser, *StartUpBlock.TITLE_STARTUP), 'Не видно заголовок блока StartUp'

    @allure.feature('Startup_block_tests')
    @allure.story('Отображение блока текста под StartUp')
    def test_visible_txt_block(self, browser, open_url):
        BasePage.scroll_to_element(self, browser, *StartUpBlock.TITLE_STARTUP)
        assert BasePage.is_visible(browser, *StartUpBlock.TEXT_BLOCK), 'Блок с текстом не отображается'


class TestHelpProjectBlock():

    @allure.feature('Help_block_tests')
    @allure.story('Отображение надписи Помочь проекту')
    def test_visible_title_help(self, browser, open_url):
        BasePage.scroll_to_element(self, browser, *HelpPjtBlock.TITLE_HELP)
        assert BasePage.is_visible(browser, *HelpPjtBlock.TITLE_HELP), 'Надпись Помочь проекту не видна'

    @allure.feature('Help_block_tests')
    @allure.story('Отображение текста в блоке')
    def test_visible_text_help(self, browser, open_url):
        BasePage.scroll_to_element(self, browser, *HelpPjtBlock.TITLE_HELP)
        assert BasePage.is_visible(browser, *HelpPjtBlock.TEXT_HELP), 'Текст в блоке Помочь проекту не виден'

    @allure.feature('Help_block_tests')
    @allure.story('Отображение кнопки Boosty')
    def test_visible_btn_boosty(self, browser, open_url):
        BasePage.scroll_to_element(self, browser, *HelpPjtBlock.BTN_BOOSTY)
        assert BasePage.is_visible(browser, *HelpPjtBlock.BTN_BOOSTY), 'Кнопка Boosty не видна'

    @allure.feature('Help_block_tests')
    @allure.story('-При нажатии на кнопку Boosty открывается страница ExLab на сайте Boosty')
    def test_btn_bsty_click(self, browser, open_url):
        BasePage.scroll_to_element(self, browser, *HelpPjtBlock.BTN_BOOSTY)
        browser.find_element(*HelpPjtBlock.BTN_BOOSTY).click()
        browser.switch_to.window(browser.window_handles[1])
        assert browser.current_url == BaseLocators.LINK_EX_BOOSTY, 'Страница не открывается'

    @allure.feature('Help_block_tests')
    @allure.story('Отображение кнопки Patreon')
    def test_visible_btn_patreon(self, browser, open_url):
        BasePage.scroll_to_element(self, browser, *HelpPjtBlock.BTN_PATREON)
        assert BasePage.is_visible(browser, *HelpPjtBlock.BTN_PATREON), 'Кнопка Patreon не видна'

    # не настроен переход на патреон
    @pytest.mark.xfail
    @allure.feature('Help_block_tests')
    @allure.story('-При нажатии на кнопку Patreon открывается страница ExLab на сайте Patreon')
    def test_btn_patreon_click(self, browser, open_url):
        BasePage.scroll_to_element(self, browser, *HelpPjtBlock.BTN_PATREON)
        browser.find_element(*HelpPjtBlock.BTN_PATREON).click()
        browser.switch_to.window(browser.window_handles[1])
        assert browser.current_url == BaseLocators.LINK_EX_BOOSTY, 'Страница не открывается'

class TestStayInTouch:

    @allure.feature('SiT_block_tests')
    @allure.story('Отображение надписи Оставайся на связи')
    def test_visible_title_SiT(self, browser, open_url):
        browser.implicitly_wait(4)
        BasePage.scroll_to_element(self, browser, *SiTBlock.TITLE_SiT)
        assert BasePage.is_visible(browser, *SiTBlock.TITLE_SiT), "Заголовка блока нет"

    @allure.feature('SiT_block_tests')
    @allure.story('Отображение текста в блоке ')
    def test_text_in_block_SiT(self, browser, open_url):
        browser.implicitly_wait(4)
        BasePage.scroll_to_element(self, browser, *SiTBlock.TITLE_SiT)
        assert BasePage.is_visible(browser, *SiTBlock.TEXT_SiT), "Текста блока нет"

class TestFutterBlock():
    @allure.feature('SiT_block_tests')
    @allure.story('Отображение логотипа ExLab')
    def test_visible_logo_fut(self, browser, open_url):
        browser.implicitly_wait(4)
        BasePage.scroll_to_element(self, browser, *FutterBlock.LOGO_FUT_EXLAB)
        assert BasePage.is_visible(browser, *FutterBlock.LOGO_FUT_EXLAB), "Логотип не отображается"

    @allure.feature('SiT_block_tests')
    @allure.story('Отображение текста под логотипом ExLab')
    def test_visible_text_under_logo(self, browser, open_url):
        browser.implicitly_wait(4)
        BasePage.scroll_to_element(self, browser, *FutterBlock.LOGO_FUT_EXLAB)
        assert BasePage.is_visible(browser, *FutterBlock.TEXT_UNDER_LOGO), "Текст под логотипом не отображается"

    @allure.feature('SiT_block_tests')
    @allure.story('Отображение ссылки LNKDN')
    def test_visible_lnkd(self, browser, open_url):
        browser.implicitly_wait(4)
        BasePage.scroll_to_element(self, browser, *FutterBlock.LOGO_FUT_EXLAB)
        assert BasePage.is_visible(browser, *FutterBlock.LNKD), "Ссылка Линкедин не от ображается"

    @allure.feature('SiT_block_tests')
    @allure.story('Ссылка ведет  на страницу ExLab в LinkedIn')
    def test_link_lnkdn(self, browser, open_url):
        browser.implicitly_wait(4)
        BasePage.scroll_to_element(self, browser, *FutterBlock.LOGO_FUT_EXLAB)
        browser.find_element(*FutterBlock.LNKD).click()
        browser.switch_to.window(browser.window_handles[1])
        assert browser.current_url == FutterBlock.URL_LNKD, 'Страница не открылась'

    @allure.feature('SiT_block_tests')
    @allure.story('Отображение ссылки INST')
    def test_visible_inst(self, browser, open_url):
        browser.implicitly_wait(4)
        BasePage.scroll_to_element(self, browser, *FutterBlock.LOGO_FUT_EXLAB)
        assert BasePage.is_visible(browser, *FutterBlock.INST), "Ссылка Инстаграм не от отображается"

    @allure.feature('SiT_block_tests')
    @allure.story('Ссылка ведет  на страницу ExLab в Instagram')
    def test_link_lnkdn(self, browser, open_url):
        browser.implicitly_wait(5)
        BasePage.scroll_to_element(self, browser, *FutterBlock.LOGO_FUT_EXLAB)
        browser.find_element(*FutterBlock.INST).click()
        browser.switch_to.window(browser.window_handles[1])
        assert browser.current_url == FutterBlock.URL_INST, 'Страница не открылась'

    @allure.feature('SiT_block_tests')
    @allure.story('Отображение ссылки TLGR')
    def test_visible_tlgr(self, browser, open_url):
        browser.implicitly_wait(5)
        BasePage.scroll_to_element(self, browser, *FutterBlock.LOGO_FUT_EXLAB)
        assert BasePage.is_visible(browser, *FutterBlock.TLGR), "Ссылка Линкедин не от ображается"

    @allure.feature('SiT_block_tests')
    @allure.story('Ссылка ведет  на страницу ExLab в Telegram')
    def test_link_tlgr(self, browser, open_url):
        browser.implicitly_wait(5)
        BasePage.scroll_to_element(self, browser, *FutterBlock.TLGR)
        browser.find_element(*FutterBlock.TLGR).click()
        # time.sleep(6)
        browser.switch_to.window(browser.window_handles[1])
        # alert_obj = browser.switch_to.alert
        # alert_obj.dismiss()
        assert browser.current_url == FutterBlock.URL_TLGR, 'Страница не открылась'

    @allure.feature('SiT_block_tests')
    @allure.story('Отображение ссылки YTB')
    def test_visible_ytb(self, browser, open_url):
        browser.implicitly_wait(5)
        BasePage.scroll_to_element(self, browser, *FutterBlock.LOGO_FUT_EXLAB)
        assert BasePage.is_visible(browser, *FutterBlock.YTB), "Ссылка Youtube не от ображается"

    @allure.feature('SiT_block_tests')
    @allure.story('Ссылка ведет  на страницу ExLab в YTB')
    def test_link_ytb(self, browser, open_url):
        browser.implicitly_wait(5)
        BasePage.scroll_to_element(self, browser, *FutterBlock.LOGO_FUT_EXLAB)
        browser.find_element(*FutterBlock.YTB).click()
        browser.switch_to.window(browser.window_handles[1])
        assert browser.current_url == FutterBlock.URL_YTB, 'Страница не открылась'

    @allure.feature('SiT_block_tests')
    @allure.story('Отображение ссылки info@exlab.team ')
    def test_visible_email(self, browser, open_url):
        browser.implicitly_wait(5)
        BasePage.scroll_to_element(self, browser, *FutterBlock.EMAIL)
        assert BasePage.is_visible(browser, *FutterBlock.EMAIL), "Ссылка email не от отображается"




