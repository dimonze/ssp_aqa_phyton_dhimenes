import allure

from page_objects.create_issue_page import CreateIssuePage
from page_objects.login_page import LoginPage
from page_objects.search_issue_page import SearchIssuePage
from page_objects.update_issue_page import UpdateIssuePage
from .utils.global_scope import *


@pytest.mark.usefixtures("driver_init")
class TestJira:

    @pytest.mark.parametrize("login,passwd,res", [
        ("Dima_Himenes", "Dima_Himene", "please try again"),
        ("Dima_Himene", "Dima_Himenes", "please try again"),
        ("Dima_Himenes", "Dima_Himenes", "System Dashboard"),
    ])
    @allure.title('Test-UI-Login-to-Jira')
    def test_ui_login_to_jira(self, login, passwd, res):
        self.driver.get(global_url_ui)
        login_page = LoginPage(self.driver)
        login_page.fill_login(login)
        login_page.fill_passwd(passwd)
        login_page.press_loginbtn()
        assert res in login_page.wait_for_result(res)

    @pytest.mark.parametrize("summary,body,res", [
        (normal_summary, normal_body, normal_summary),
        (empty_summary, normal_body, "summary: You must specify a summary of the issue."),
        (to_long_summary, normal_body, "summary: Summary must be less than 255 characters."),
    ])
    @allure.title('Test-UI-Create-issue')
    def test_ui_create_issue(self, summary, body, res):
        self.driver.get(global_url_ui + 'secure/CreateIssue!default.jspa?' + global_auth)

        create_issue_page = CreateIssuePage(self.driver)
        create_issue_page.press_nextbtn()
        create_issue_page.fill_summary(summary)
        create_issue_page.fill_body(body)
        create_issue_page.press_createbtn()
        create_issue_page.wait_for_result(res)
        assert res in create_issue_page.wait_for_result(res)

    @pytest.mark.parametrize("search_jql,res", [
        ('project%20%3D%20AQAPYTHON%20AND%20text%20~%20"AQAPYTHON-6"', 1),
        ('project%20%3D%20AQAPYTHON%20AND%20text%20~%20"AQAPYTHON-0"', 0),
        ('project%20%3D%20AQAPYTHON%20AND%20text%20~%20"superIDis*"', 5),
    ])
    @allure.title('Test-UI-Search-issue')
    def test_ui_search_issue(self, search_jql, res):
        self.driver.get(global_url_ui + '?' + global_auth)
        self.driver.get(global_url_ui + 'browse/XH-144?jql=' + search_jql)

        search_issue_page = SearchIssuePage(self.driver)
        assert res == search_issue_page.get_count_of_issues()

    @pytest.mark.parametrize("summary,priority,assignee,issue_id,res", [
        ('New Summary', '', '', 'AQAPYTHON-721', 'AQAPYTHON-721 has been updated.'),
        ('', 'High', '', 'AQAPYTHON-721', 'AQAPYTHON-721 has been updated.'),
        ('', '', 'DIma_Himenes', 'AQAPYTHON-721', 'AQAPYTHON-721 has been updated.'),
    ])
    @allure.title('Test-UI-Update-issue')
    def test_ui_update_issue(self, summary, priority, assignee, issue_id,  res):
        self.driver.get(global_url_ui + 'browse/' + issue_id + '?' + global_auth)
        update_issue_page = UpdateIssuePage(self.driver)
        update_issue_page.press_editbtn()
        update_issue_page.fill_summary(summary)
        update_issue_page.select_prio(priority)
        update_issue_page.select_assignee(assignee)
        update_issue_page.press_updatebtn()
        assert res in update_issue_page.wait_for_result(res)
