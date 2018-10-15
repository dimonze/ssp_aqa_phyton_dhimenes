import allure

from page_objects.basic_page import BasicPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CreateIssuePage(BasicPage):
    PROJECT_INPUT = (By.CSS_SELECTOR, "#project-field")
    ISSUE_TYPE_INPUT = (By.CSS_SELECTOR, "#issuetype-field")
    DESCR_INPUT = (By.CSS_SELECTOR, "#description")
    SUMMARY_INPUT = (By.CSS_SELECTOR, "#summary")
    PRIO_INPUT = (By.CSS_SELECTOR, "#priority-field")
    ASSIGNEE_INPUT = (By.CSS_SELECTOR, "#assignee-field")
    CREATE_BTN = (By.CSS_SELECTOR, "#issue-create-submit")
    NEXT_BTN = (By.CSS_SELECTOR, "#issue-create-submit")

    @allure.step
    def press_nextbtn(self):
        self.wait.until(EC.visibility_of_element_located(self.NEXT_BTN)).click()

    @allure.step
    def fill_summary(self, value):
        self.wait.until(EC.visibility_of_element_located(self.SUMMARY_INPUT)).send_keys(value)

    @allure.step
    def fill_body(self, value):
        self.wait.until(EC.visibility_of_element_located(self.DESCR_INPUT)).send_keys(value)

    @allure.step
    def press_createbtn(self):
        self.wait.until(EC.visibility_of_element_located(self.CREATE_BTN)).click()

    @allure.step
    def wait_for_result(self, result):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(.,'" + result + "')]"))).text


