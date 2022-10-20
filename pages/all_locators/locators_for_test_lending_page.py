from selenium.webdriver.common.by import By

class BaseLocators():
    LENDING_LINK = 'http://test.exlab.team/#'
    REGISTRATION_BOT = 'https://t.me/ExLab_registration_bot'

class HeadersLocators():
    HEADER_LENDING = (By.XPATH, '//div[@id="header"]')
    LOGO_PIC_EXLAB = (By.XPATH, '(//div[@id="logo_mobile"])[1]')
    HEADER_LINK_ABOUT = (By.XPATH, '//a[@data-scroll-to="#about"]')
    HEADER_LINK_PROJECTS = (By.XPATH, '//a[@data-scroll-to="#projects"]')
    SWITCH_LIGHT_THEME = (By.XPATH, '//div[@class="sc-fnykZs fEkGUM"]')
    LIGHT_THEME = (By.XPATH, '//div[@class ="sc-bczRLJ cxdoLY"]')
    PARAGRAPH_ABOUT = (By.XPATH, '//div[@id="about"]')
    PARAGRAPH_PROJECT = (By.XPATH, '//div[@id="projects"]')
    HEADER_LINK_MENTORS = (By.XPATH, '//a[@data-scroll-to="#mentors"]')
    PARAGRAPH_MENTORS = (By.XPATH, '//*[@id="mentors"]/div[1]')
    HEADER_LINK_STARTUP = (By.XPATH, '//a[@data-scroll-to="#startup"]')
    PARAGRAPH_STARTUP_FOR = (By.XPATH, '//div[@data-scroll-target="#startup"]')
    JOIN_BUTTON = (By.XPATH, '//div[@class="sc-hAZoDl hrEelO"]')

class PossibilityBlock():
    LOGO_EXLAB = (By.XPATH, '//img[@class="sc-dIouRR iBavKg"]')
    TITLE_POSSIBILITY = (By.XPATH, '//div[@class="sc-kgflAQ gupdxc"]')
    TEXT_UNDO_TITLE = (By.XPATH, '//div[@class="sc-bBrHrO lmeoyY"]')

class AboutUsBlock():
    TITLE_ABOUT = (By.XPATH, '//div[@class="sc-himrzO bOhFlH"]/div[1]')
    TEXT_UNDO_TITLE = (By.XPATH, '//p[@class="sc-cCsOjp cdaqyF"]')
    TITLE_WHY = (By.XPATH, '//div[@class="sc-jdAMXn iDQeOI"]/div[1]')
    TEXT_UNDO_WHY = (By.XPATH, '//div[@class="sc-jdAMXn iDQeOI"]/ol')
    JOIN_BTN = (By.XPATH, '//div[@class="sc-iTONeN egXhsc"]//a')

class AllProjectBlock():
    TITLE_PROJECT = (By.XPATH, '//div[@id="projects"]/div[1]')
    PIC_EXLAB = (By.XPATH, '//img[@alt="ExLab"]')
    PIC_HL = (By.XPATH, '//img[@alt="Healthy life "]')
    PIC_EH = (By.XPATH, '//img[@alt="Easyhelp "]')






    INST = (By.XPATH, '//a[@href="https://www.instagram.com/exlab_startup/"]')




