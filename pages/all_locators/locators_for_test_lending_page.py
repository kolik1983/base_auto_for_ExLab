from selenium.webdriver.common.by import By

class BaseLocators():
    LENDING_LINK = 'http://test.exlab.team/#'

class HeadersLendingPageLocators():
    HEADER_LENDING = (By.XPATH, '//div[@id="header"]')
    LOGO_PIC_EXLAB = (By.XPATH, '//div[@class="sc-jqUVSM EnPDN"]')
    HEADER_LINK_ABOUT = (By.XPATH, '//a[@data-scroll-to="#about"]')
    HEADER_LINK_PROJECTS = (By.XPATH, '//a[@data-scroll-to="#projects"]')
