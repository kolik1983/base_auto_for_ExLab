from selenium.webdriver.common.by import By

class BaseLocators():
    LENDING_LINK = 'http://test.exlab.team/#'

class HeadersLendingPageLocators():
    HEADER_LENDING = (By.XPATH, '//div[@id="header"]')
    LOGO_PIC_EXLAB = (By.XPATH, '(//div[@id="logo_mobile"])[1]')
    HEADER_LINK_ABOUT = (By.XPATH, '//a[@data-scroll-to="#about"]')
    HEADER_LINK_PROJECTS = (By.XPATH, '//a[@data-scroll-to="#projects"]')
    SWITCH_WHITE_THEME = (By.XPATH, '//div[@class="sc-fnykZs fEkGUM"]')
    PARAGRAPH_ABOUT = (By.XPATH, '//div[@id="about"]')
    PARAGRAPH_PROJECT = (By.XPATH, '//div[@id="projects"]')
    
    


