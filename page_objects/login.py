import pytest
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def platform(request):
    return request.config.getoption("--platform")


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        # Common Locators
        self.mobile_number = (By.ID, "com.toro.Mobile-Automation:id/email_edit_text")
        self.otp = (By.ID, "com.toro.Mobile-Automation:id/password_edit_text")
        self.continue_btn = (By.ID, "com.toro.Mobile-Automation:id/sign_in_btn")
        self.error_message = (By.ID, "com.toro.Mobile-Automation:id/error_message")

    def enter_mobile_number(self, number):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.mobile_number)).send_keys(number)

    def enter_otp(self, otp):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.otp)).send_keys(otp)

    def click_continue(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.continue_btn)).click()

    def get_error_message(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.error_message)).text