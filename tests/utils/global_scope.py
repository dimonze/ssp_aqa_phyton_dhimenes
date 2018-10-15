import time

import pytest
import requests

from tests.utils.json_objs import JsonObj
from selenium import webdriver
from main_app import *
from random import randint
from .api_wrapper import ApiWrapper

global_user = 'Dima_Himenes'
global_pass = 'Dima_Himenes'
global_url = "http://jira.hillel.it:8080/rest/api/2/"
global_url_ui = "http://jira.hillel.it:8080/"
global_auth = "os_username=" + global_user + "&os_password=" + global_pass
global_headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic RGltYV9IaW1lbmVzOkRpbWFfSGltZW5lcw=="
}

rest_api = ApiWrapper()

normal_summary = 'REST ye merry gentlemen.'
normal_body = 'Creating of an issue using project keys and issue type names using the REST API 2'
empty_summary = ''
to_long_summary = 'zxczxcaaaaaaaaaaaaaaaaaaaaaaaaaaxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
