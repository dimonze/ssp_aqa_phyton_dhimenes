from .utils.global_scope import *


def test_positive():
    assert generate_fibonacci(3) == [1, 1, 2]


def test_negative():
    assert generate_fibonacci(3) != [1, 1, 3]


@pytest.mark.parametrize("login,passwd,res", [
    ("Dima_Himenes", "Dima_Himene", 401),
    ("Dima_Himene", "Dima_Himenes", 401),
    ("Dima_Himenes", "Dima_Himenes", 200),
])
def test_login_to_jira(login, passwd, res):
    assert res == rest_api.login_to_jira_api(login, passwd).status_code


@pytest.mark.parametrize("file_name,res", [
    ("create_issue.json", 201),
    ("create_issue_long_text.json", 400),
    ("create_issue_missing_field.json", 400),
])
def test_create_issue(file_name, res):
    assert res == rest_api.create_issue_api(file_name).status_code


@pytest.mark.parametrize("search_jql,res", [
    ('project%20%3D%20AQAPYTHON%20AND%20text%20~%20"AQAPYTHON-6"', 1),
    ('project%20%3D%20AQAPYTHON%20AND%20text%20~%20"AQAPYTHON-0"', 0),
    ('project%20%3D%20AQAPYTHON%20AND%20text%20~%20"superIDis*"', 5),
])
def test_search_issue(search_jql, res):
    assert res == rest_api.search_issue_api(search_jql).json()['total']


@pytest.mark.parametrize("file_name,issue_id,res", [
    ('update_issue_summary.json', 'AQAPYTHON-5', 204),
    ('update_issue_priority.json', 'AQAPYTHON-5', 204),
    ('update_issue_assignee.json', 'AQAPYTHON-5', 204),
])
def test_update_issue(file_name, issue_id, res):
    assert res == rest_api.update_issue_api(file_name, issue_id).status_code

