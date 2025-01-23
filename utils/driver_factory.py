from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
import pytest

def pytest_addoption(parser):
    parser.addoption("--platorm", action="store", default="iOS", help="Platorm")

@pytest.fixture
def platform(request):
    return request.config.getoption("--platform")

@pytest.fixture
def get_driver(platform):
    desired_caps = {}
    if platform == 'Android':
        desired_caps = {
            
            "platformname" : 'Android',
            "platformVersion" : '13',
            "deviceName" : "Pixel-4a",
            "automationName" : 'Appium',
            "app" : "/Users/sharadbagul/Downloads/app-stage1.apk",
            "noReset" : False
            # appWaitActivity : "com.toro.Mobile-Automation.modules.login.view.LoginActivity"
            # app_wait_package : "com.toro.Mobile-Automation"
        }
        # options = UiAutomator2Options()
        # options.platform_name = 'Android'
        # options.platform_version = '13'
        # options.udid = uid
        # options.system_port = port
        # options.device_name = "Pixel-4a"
        # options.automation_name = 'Appium'
        # options.app = "/Users/sharadbagul/Downloads/app-stage1.apk"
        # options.no_reset = False
        # options.app_wait_activity = "com.toro.Mobile-Automation.modules.login.view.LoginActivity"
        # options.app_wait_package = "com.toro.Mobile-Automation"

        # driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)
    elif platform == 'iOS':
        desired_caps = {
        "appium:platformName": "iOS",
        "appium:automationName": "xcuitest",
        "appium:device": "iPhone",
        "appium:udid": uid,
        "appium:deviceName": "iPhone",
        "appium:platformVersion": "17.5",
        "appium:newCommandTimeout": 10000,
        "appium:app": "/Users/sharadbagul/Downloads/Mobile-Automation(1).ipa"
        # "appium:app_wait_activity" : "com.toro.Mobile-Automation.modules.login.view.LoginActivity",
        # "appium:app_wait_package" : "com.toro.Mobile-Automation"
        }
    else:
        raise ValueError("Some error occured")


    # capabilities_options = XCUITestOptions().load_capabilities(desired_capabilities)
    driver = webdriver.Remote("http://localhost:4723/wd/hub", options=desired_caps)
    yield driver
    driver.quit()
    # return driver
# emulator-5554 