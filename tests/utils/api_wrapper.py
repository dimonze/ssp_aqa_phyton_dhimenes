import requests

from tests.utils.json_objs import JsonObj

global_user = 'Dima_Himenes'
global_pass = 'Dima_Himenes'
global_url = "http://jira.hillel.it:8080/rest/api/2/"
global_url_ui = "http://jira.hillel.it:8080/"
global_auth = "os_username=" + global_user + "&os_password=" + global_pass
global_headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic RGltYV9IaW1lbmVzOkRpbWFfSGltZW5lcw=="
}


class ApiWrapper:

    @staticmethod
    def login_to_jira_api(login, passwd):
        return requests.get(global_url + 'issue/XH-144', auth=(login, passwd))

    @staticmethod
    def create_issue_api(file_name):
        return requests.request("POST", global_url + 'issue/', data=JsonObj(file_name).read_json(),
                                headers=global_headers)

    @staticmethod
    def search_issue_api(search_jql):
        return requests.request("GET", global_url + 'search?jql=' + search_jql, auth=(global_user, global_pass))

    @staticmethod
    def update_issue_api(file_name, issue_id):
        return requests.request("PUT", global_url + 'issue/' + issue_id, data=JsonObj(file_name).read_json(),
                                headers=global_headers)
