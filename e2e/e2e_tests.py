from selenium import webdriver
import variables
import pytest
from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from assertions.login_page_assertions import LoginPageAssertions
from assertions.secure_page_assertions import SecurePageAssertions

class TestLoginPage:
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, request):
        driver = webdriver.Chrome()
        driver.get(variables.LOGIN_URL)
        request.cls.driver = driver
        yield
        driver.quit()
    
    def test_login_form_visible(self):
        login_page = LoginPage(self.driver)
        
        LoginPageAssertions(login_page).assert_login_form_visible()
        
    def test_login_with_valid_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.login(variables.LOGIN_USERNAME, variables.LOGIN_PASSWORD)
        secure_page = SecurePage(self.driver)
        
        SecurePageAssertions(secure_page).assert_that_user_is_logged_in()
        
    def test_logout(self):
        login_page = LoginPage(self.driver)
        login_page.login(variables.LOGIN_USERNAME, variables.LOGIN_PASSWORD)
        
        secure_page = SecurePage(self.driver)
        secure_page.logout()
        
        LoginPageAssertions(login_page).assert_that_user_has_logged_out()
        
    def test_login_with_invalid_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.login("invalid_user", "invalid_password")
        
        LoginPageAssertions(login_page).assert_that_invalid_login_flash_message_is_displayed()

        
