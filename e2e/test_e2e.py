from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import e2e_variables
import pytest
from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from assertions.login_page_assertions import LoginPageAssertions
from assertions.secure_page_assertions import SecurePageAssertions

class TestLoginPage:
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, request):
        chrome_options = Options()
        if e2e_variables.RUN_HEADLESS == True:
            chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(e2e_variables.LOGIN_URL)
        request.cls.driver = driver
        yield
        driver.quit()
    
    def test_login_form_visible(self):
        login_page = LoginPage(self.driver)
        
        LoginPageAssertions(login_page).assert_login_form_visible()
        
    def test_login_with_valid_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.login(e2e_variables.LOGIN_USERNAME, e2e_variables.LOGIN_PASSWORD)
        secure_page = SecurePage(self.driver)
        
        SecurePageAssertions(secure_page).assert_that_user_is_logged_in()
        
    def test_logout(self):
        login_page = LoginPage(self.driver)
        login_page.login(e2e_variables.LOGIN_USERNAME, e2e_variables.LOGIN_PASSWORD)
        
        secure_page = SecurePage(self.driver)
        secure_page.logout()
        
        LoginPageAssertions(login_page).assert_that_user_has_logged_out()
        
    def test_login_with_invalid_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.login("invalid_user", "invalid_password")
        
        LoginPageAssertions(login_page).assert_that_invalid_login_flash_message_is_displayed()

        
