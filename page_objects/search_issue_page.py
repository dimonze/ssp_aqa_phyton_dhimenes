from selenium.common.exceptions import TimeoutException

from page_objects.basic_page import BasicPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SearchIssuePage(BasicPage):
    ISSUES_LIST = (By.CSS_SELECTOR, "ol.issue-list li")

    def get_count_of_issues(self):
        try:
            return len(self.wait.until(EC.visibility_of_all_elements_located(self.ISSUES_LIST)))
        except TimeoutException:
            return 0




