import pytest
import allure
from page_objects.login import LoginPage
from utils.driver_factory import get_driver

@allure.feature("Login Functionality")
class TestLogin:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)

    @allure.story("Successful Login")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_login(self):
        with allure.step("Enter valid mobile number"):
            self.login_page.enter_mobile_number("valid_user")

        with allure.step("Enter valid OTP"):
            self.login_page.enter_otp("valid_otp")

        with allure.step("Click continue button"):
            self.login_page.click_continue()

        with allure.step("Validate successful login"):
            assert "Home" in self.driver.page_source, "Login failed despite valid credentials."

    @allure.story("Invalid Login")
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_login(self):
        with allure.step("Enter invalid mobile number"):
            self.login_page.enter_mobile_number("invalid_user")

        with allure.step("Enter invalid OTP"):
            self.login_page.enter_otp("wrong_otp")

        with allure.step("Click continue button"):
            self.login_page.click_continue()

        with allure.step("Validate error message"):
            error_message = self.login_page.get_error_message()
            assert error_message == "Invalid credentials", f"Unexpected error message: {error_message}"