import pytest
import requests

from json_objs import JsonObj
from main_app import *
from random import randint

global_user = 'Dima_Himenes'
global_pass = 'Dima_Himenes'
global_url = "http://jira.hillel.it:8080/rest/api/2/"
global_headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic RGltYV9IaW1lbmVzOkRpbWFfSGltZW5lcw=="
}


def test_positive():
    assert generate_fibonacci(3) == [1, 1, 2]


def test_negative():
    assert not generate_fibonacci(3) == [1, 1, 3]


@pytest.mark.parametrize("login,passwd,res", [
    ("Dima_Himenes", "Dima_Himene", 401),
    ("Dima_Himene", "Dima_Himenes", 401),
    ("Dima_Himenes", "Dima_Himenes", 200),
])
def test_login_to_jira(login, passwd, res):
    assert res == requests.get(global_url + 'issue/XH-144', auth=(login, passwd)).status_code


@pytest.mark.parametrize("file_name,res", [
    ("create_issue.json", 201),
    ("create_issue_long_text.json", 400),
    ("create_issue_missing_field.json", 400),
])
def test_create_issue(file_name, res):
    assert res == requests.request("POST", global_url + 'issue/', data=JsonObj(file_name).read_json(),
                                   headers=global_headers).status_code


@pytest.mark.parametrize("search_jql,res", [
    ('project%20%3D%20AQAPYTHON%20AND%20text%20~%20"AQAPYTHON-6"', 1),
    ('project%20%3D%20AQAPYTHON%20AND%20text%20~%20"AQAPYTHON-0"', 0),
    ('project%20%3D%20AQAPYTHON%20AND%20text%20~%20"superIDis*"', 5),
])
def test_search_issue(search_jql, res):
    assert res == requests.request("GET", global_url + 'search?jql=' + search_jql,
                                   auth=(global_user, global_pass)).json()['total']


@pytest.mark.parametrize("file_name,issue_id,res", [
    ('update_issue_summary.json', 'AQAPYTHON-5', 204),
    ('update_issue_priority.json', 'AQAPYTHON-5', 204),
    ('update_issue_assignee.json', 'AQAPYTHON-5', 204),
])
def test_update_issue(file_name, issue_id, res):
    assert res == requests.request("PUT", global_url + 'issue/' + issue_id, data=JsonObj(file_name).read_json(),
                                   headers=global_headers).status_code


def test_random():
    assert randint(1, 2) == 2
