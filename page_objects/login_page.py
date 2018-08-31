import allure

from page_objects.basic_page import BasicPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage(BasicPage):
    LOGIN_INPUT = (By.CSS_SELECTOR, "input[name='os_username']")
    PASWD_INPUT = (By.CSS_SELECTOR, "input[name='os_password']")
    LOGIN_BTN = (By.CSS_SELECTOR, "input[name='login']")

    @allure.step
    def fill_login(self, value):
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_INPUT)).send_keys(value)

    @allure.step
    def fill_passwd(self, value):
        self.wait.until(EC.visibility_of_element_located(self.PASWD_INPUT)).send_keys(value)

    @allure.step
    def press_loginbtn(self):
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_BTN)).click()

    @allure.step
    def wait_for_result(self, result):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(.,'" + result + "')]"))).text


