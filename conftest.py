import pytest


@pytest.fixture(scope="class")
def driver_init(request):
    from selenium import webdriver
    options = webdriver.ChromeOptions()
    options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    chrome_driver_binary = "./drivers/chromedriver"
    web_driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
    request.cls.driver = web_driver
    yield
    web_driver.close()
