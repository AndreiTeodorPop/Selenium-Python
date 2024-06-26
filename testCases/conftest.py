from selenium import webdriver
from pytest_metadata.plugin import metadata_key
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome browser...........")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox browser...........")
    else:
        driver = webdriver.Edge()
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


####################### PyTest HTML Report #########################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "Selenium Python"
    config.stash[metadata_key]["Module Name"] = "Customers"
    config.stash[metadata_key]["Tester"] = "Andrei"


# It is hook for delete/modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
