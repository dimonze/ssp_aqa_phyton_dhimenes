from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver


class BasicPage(object):
    def __init__(self, driver: WebDriver, ):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
