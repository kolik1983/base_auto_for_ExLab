from selenium.webdriver.common.by import By

class BaseLocators():
    LENDING_LINK = 'http://test.exlab.team/#'
    REGISTRATION_BOT = 'https://t.me/ExLab_registration_bot'
    LINK_EX_BOOSTY = (By.XPATH, 'https://boosty.to/exlab_startup')

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
    THREE_LOGO = (By.XPATH, '//img[@class="sc-bBXxYQ hEflMO"]')
    THREE_TEXT_BLOCK = (By.XPATH, '//div[@class="sc-lbxAil jbFjXS"]/div/p')

class MentorsBlock():
    TITLE_MENTORS = (By.XPATH, '//div[@id="mentors"]/div[1]')
    AREA_MENTOR1 = (By.XPATH, '//div[@class="sc-jIAOiI kQWCrM"]/div[1]')
    AREA_MENTOR2 = (By.XPATH, '//div[@class="sc-jIAOiI kQWCrM"]/div[2]')
    AREA_MENTOR3 = (By.XPATH, '//div[@class="sc-jIAOiI kQWCrM"]/div[3]')
    AREA_MENTOR4 = (By.XPATH, '//div[@class="sc-jIAOiI kQWCrM"]/div[4]')
    SPOILER_MENTOR = (By.XPATH, '//div[@class="sc-kIKDeO hGmlWc"]')
    PHOTOS_MENTORS = (By.XPATH, '//img[@class="sc-hNKHps bLOuOe"]')
    DESCRIPTIONS_MENTORS = (By.XPATH, '//ul[@class="sc-cZwWEu kmkvji"]')
    CLOSE_AREA = (By.XPATH, '//div[@class="sc-kIKDeO hGmlWc"]')
    # BUTTON_BEC_MENTOR = (By.XPATH, '') no locator)

class StartUpBlock():

    TITLE_STARTUP = (By.XPATH, '//div[@data-scroll-target="#startup"]')
    TEXT_BLOCK = (By.XPATH, '//div[@class="sc-eKszNL gOjGBb"]')

class HelpPjtBlock():

    TITLE_HELP = (By.XPATH, '//div[@class="sc-jTYCaT NkTuJ"]/div[1]')
    TEXT_HELP = (By.XPATH, '//div[@class="sc-fvNpTx eJpwBO"]')
    BTN_BOOSTY = (By.XPATH, '//a[@href="https://boosty.to/exlab_startup"]')
    BTN_PATREON = (By.XPATH, '//a[@class="sc-hKMtZM etdNbW"]')










    # INST = (By.XPATH, '//a[@href="https://www.instagram.com/exlab_startup/"]')




