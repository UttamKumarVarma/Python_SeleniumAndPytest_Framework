import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


driver = None

#gets browser details from terminal
def pytest_addoption(parser):
    parser.addoption("--browser_name", action= "store", default="chrome")


@pytest.fixture(scope="class")
def browserSetup(request):
    global driver
    # Get the current directory of this script
    #PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    #DRIVER_PATH = os.path.join(PROJECT_ROOT, "../drivers/chromedriver")
    #service_object = Service(DRIVER_PATH)
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        #driver = webdriver.Chrome(service=service_object)
        driver = webdriver.Chrome()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    elif browser_name == "firefox":
        driver= webdriver.Firefox()
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)
