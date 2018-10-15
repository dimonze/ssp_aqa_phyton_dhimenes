import pytest
import os
import allure


@pytest.fixture(scope="class")
def driver_init(request):
    from selenium import webdriver
    options = webdriver.ChromeOptions()
    if os.name == 'nt':
        web_driver = webdriver.Chrome("./drivers/chromedriver.exe")
    else:
        options.binary_location = "/usr/bin/google-chrome"
        chrome_driver_binary = "./drivers/chromedriver"
        web_driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        try:
            if 'driver_init' in item.fixturenames:
                web_driver = item.funcargs['request'].instance.driver
            else:
                return
            web_driver.execute_script("document.body.bgColor = 'white';")

            allure.attach(web_driver.get_screenshot_as_png(),
                          name=item.name,
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print('Exception while screen-shot creation: {}'.format(e))
