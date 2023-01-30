from selenium.webdriver.common.by import By

class BaseLocators():
    LENDING_LINK = 'http://test.exlab.team/#'
    REGISTRATION_BOT = 'https://t.me/ExLab_registration_bot'
    LINK_EX_BOOSTY = 'https://boosty.to/exlab_startup'
    FOOTER = (By.XPATH, '//div[@class="sc-evrZIY hdIkLU"]')

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
    PARAGRAPH_MENTORS = (By.XPATH, '//div[@id="mentors"]')
    HEADER_LINK_STARTUP = (By.XPATH, '//a[@href="#startup"]')
    PARAGRAPH_STARTUP_FOR = (By.XPATH, '//div[@id="startup-title-wrapper"]/div')
    JOIN_BUTTON = (By.XPATH, '//div[@class="sc-hAZoDl hrEelO"]')

class PossibilityBlock():
    LOGO_EXLAB = (By.XPATH, '//img[@class="sc-idiyUo gJxphU"]')
    TITLE_POSSIBILITY = (By.XPATH, '//div[@class="sc-dmRaPn ljhwJa"]')
    TEXT_UNDO_TITLE = (By.XPATH, '//div[@class="sc-kgflAQ gUFAgN"]')

class AboutUsBlock():
    TITLE_ABOUT = (By.XPATH, '//div[@class="sc-ikZpkk fAmEjI"]/div[1]')
    TEXT_UNDO_TITLE = (By.XPATH, '//p[@class="sc-himrzO bgsrpw"]')
    TITLE_WHY = (By.XPATH, '//div[@class="sc-ciZhAO fBFmnR"]')
    TEXT_UNDO_WHY = (By.XPATH, '//ol[@class="sc-bZnhIo fYGDkJ"]')
    JOIN_BTN = (By.XPATH, '//div[@class="sc-jdAMXn gLqyEH"]/a')

class AllProjectBlock():
    TITLE_PROJECT = (By.XPATH, '//div[@id="projects"]/div[1]')
    PIC_EXLAB = (By.XPATH, '//img[@alt="ExLab"]')
    PIC_HL = (By.XPATH, '//img[@alt="Healthy life "]')
    PIC_EH = (By.XPATH, '//img[@alt="Easyhelp "]')
    THREE_LOGO = (By.XPATH, '//img[@class="sc-jOrMOR eGXkMj"]')
    THREE_TEXT_BLOCK = (By.XPATH, '//p[@class="sc-dPyBCJ elZmsx"]')

class MentorsBlock():
    TITLE_MENTORS = (By.XPATH, '//div[@id="mentors"]/div[1]')
    SPOILERS_MENTOR = (By.XPATH, '//div[@class="sc-jIAOiI eSpxWu"]')
    PHOTOS_MENTORS = (By.XPATH, '//img[@class="sc-kIKDeO oyXhj"]')
    DESCRIPTIONS_MENTORS = (By.XPATH, '//ul[@class="sc-dsQDmV iZMcmm"]')
    CLOSE_AREA = (By.XPATH, '//div[@class="sc-ZyCDH kgnDMn"]')
    HIDDEN_AREA = (By.XPATH, '//div[@class="sc-bUbCnL fJhsUc"]')

class StartUpBlock():

    TITLE_STARTUP = (By.XPATH, '//div[@class="sc-iNWwEs eMChwx"]/div[1]')
    TEXT_BLOCK = (By.XPATH, '//div[@class="sc-lbxAil bXZnGi"]')

class HelpPjtBlock():

    TITLE_HELP = (By.XPATH, '//div[@class="sc-jTYCaT coDMnK"]')
    TEXT_HELP = (By.XPATH, '//div[@class="sc-fctJkW gfwicC"]')
    BTN_BOOSTY = (By.XPATH, '//a[@href="https://boosty.to/exlab_startup"]')
    BTN_PATREON = (By.XPATH, '//a[@class="sc-hKMtZM etdNbW"]')

class SiTBlock():

    TITLE_SiT = (By.XPATH, '//div[@class="sc-bhVIhj uaVnA"]')
    TEXT_SiT = (By.XPATH, '//div[@class="sc-eGAhfa cacMWv"]')

class FutterBlock():

    LOGO_FUT_EXLAB = (By.XPATH, '//div[@class="sc-fIavCj fEzmxG"]')
    TEXT_UNDER_LOGO = (By.XPATH, '//div[@class="sc-gITdmR hYaavu"]')
    LNKD = (By.XPATH, '//a[@href="https://www.linkedin.com/company/exlab-start-up/mycompany/"]')
    URL_LNKD = 'https://www.linkedin.com/company/exlab-start-up/mycompany/'
    INST = (By.XPATH, '//a[@href="https://www.instagram.com/exlab_startup/"]')
    URL_INST = 'https://www.instagram.com/exlab_startup/'
    TLGR = (By.XPATH, '//a[@href="https://t.me/ExLabChannel"]')
    URL_TLGR = 'https://t.me/ExLabChannel'
    YTB = (By.XPATH, '//a[@href="https://www.youtube.com/channel/UC-TAnVYVN7qg5dgsYQJkuvA"]')
    URL_YTB = 'https://www.youtube.com/channel/UC-TAnVYVN7qg5dgsYQJkuvA'
    EMAIL = (By.XPATH, '//a[@href="mailto:info@exlab.team"]')


