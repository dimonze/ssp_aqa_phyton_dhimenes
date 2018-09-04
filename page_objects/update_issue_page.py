from page_objects.basic_page import BasicPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class UpdateIssuePage(BasicPage):
    PROJECT_INPUT = (By.CSS_SELECTOR, "#project-field")
    ISSUE_TYPE_INPUT = (By.CSS_SELECTOR, "#issuetype-field")
    DESCR_INPUT = (By.CSS_SELECTOR, "#description")
    SUMMARY_INPUT = (By.CSS_SELECTOR, "#summary")
    PRIO_INPUT = (By.CSS_SELECTOR, "#priority-field")
    ASSIGNEE_INPUT = (By.CSS_SELECTOR, "#assignee-field")
    UPDATE_BTN = (By.CSS_SELECTOR, "#edit-issue-submit")
    EDIT_BTN = (By.CSS_SELECTOR, "#edit-issue")

    def press_editbtn(self):
        self.wait.until(EC.visibility_of_element_located(self.EDIT_BTN)).click()

    def fill_summary(self, value):
        if len(value) < 1:
            return True
        self.wait.until(EC.visibility_of_element_located(self.SUMMARY_INPUT)).clear()
        self.wait.until(EC.visibility_of_element_located(self.SUMMARY_INPUT)).send_keys(value)

    def select_assignee(self, value):
        if len(value) < 1:
            return True
        self.wait.until(EC.visibility_of_element_located(self.ASSIGNEE_INPUT)).send_keys(value)

    def select_prio(self, value):
        if len(value) < 1:
            return True
        self.wait.until(EC.visibility_of_element_located(self.PRIO_INPUT)).send_keys(value)

    def press_updatebtn(self):
        self.wait.until(EC.visibility_of_element_located(self.UPDATE_BTN)).click()

    def wait_for_result(self, result):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(.,'" + result + "')]"))).text
