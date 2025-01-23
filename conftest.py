from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
import pytest
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# -- Conftest.py Configuration

def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default="Android", help="Platform to test on: Android or iOS")

@pytest.fixture(scope="session")
def platform(request):
    return request.config.getoption("--platform")

@pytest.fixture(scope="class")
def driver(platform):
    if platform == 'Android':
        desired_caps = {
            "platformName": "Android",
            "appium:deviceName": "Galaxy M14 5G",
            "appium:app": "/home/yashu/Downloads/app-release.apk",
            "appium:automationName": "UiAutomator2",
            "appium:appPackage": "org.idreameducation.iprepapp",
            "appium:noReset": True,
            "appium:newCommandTimeout": 3600,
            "appium:unicodeKeyboard": True,
            "appium:resetKeyboard": True,
        }
    elif platform == 'iOS':
        desired_caps = {
            "platformName": "iOS",
            "appium:automationName": "XCUITest",
            "appium:deviceName": "iPhone",
            "appium:platformVersion": "17.5",
            "appium:newCommandTimeout": 3600,
            "appium:app": "/path/to/Mobile-Automation.ipa"
        }
    else:
        raise ValueError("Unsupported platform. Use 'Android' or 'iOS'.")

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    yield driver
    driver.quit()   