from selenium import webdriver
import variables
import pytest
from pages.login_page import LoginPage
from pages.secure_page import SecurePage

class TestLoginPage:
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, request):
        driver = webdriver.Chrome()
        driver.get(variables.LOGIN_URL)
        request.cls.driver = driver  # Attach driver to the class
        yield
        driver.quit()
    
    def test_login_form_visible(self):
        login_page = LoginPage(self.driver)
        
        assert login_page.username_input.is_displayed(), "Username input is not visible"
        assert login_page.password_input.is_displayed(), "Password input is not visible"
        assert login_page.login_button.is_displayed(), "Login button is not visible"
        
    def test_login_with_valid_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.login(variables.LOGIN_USERNAME, variables.LOGIN_PASSWORD)
        secure_page = SecurePage(self.driver)
        
        assert secure_page.flash_messages.is_displayed(), "Flash messages are not displayed"
        assert "You logged into a secure area!" in secure_page.flash_messages.text, "Login failed or flash message not as expected"
        
    def test_logout(self):
        login_page = LoginPage(self.driver)
        login_page.login(variables.LOGIN_USERNAME, variables.LOGIN_PASSWORD)
        
        secure_page = SecurePage(self.driver)
        secure_page.logout()
        
        assert secure_page.flash_messages.is_displayed(), "Flash messages are not displayed after logout"
        assert "You logged out of the secure area!" in secure_page.flash_messages.text, "Logout failed or flash message not as expected"
        
    def test_login_with_invalid_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.login("invalid_user", "invalid_password")
        
        assert login_page.flash_messages.is_displayed(), "Flash messages are not displayed"
        assert "Your username is invalid!" in login_page.flash_messages.text, "Flash message for invalid login not as expected"

        
