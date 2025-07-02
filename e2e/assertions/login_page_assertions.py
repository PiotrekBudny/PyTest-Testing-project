class LoginPageAssertions:
    def __init__(self, page):
        self.page = page

    def assert_login_form_visible(self):
        assert self.page.username_input.is_displayed(), "Username input is not visible"
        assert self.page.password_input.is_displayed(), "Password input is not visible"
        assert self.page.login_button.is_displayed(), "Login button is not visible"
        
    def assert_that_invalid_login_flash_message_is_displayed(self):
        assert self.page.flash_messages.is_displayed(), "Flash messages are not displayed"
        assert "Your username is invalid!" in self.page.flash_messages.text, "Flash message for invalid login not as expected"
        
    def assert_that_user_has_logged_out(self):
        assert self.page.flash_messages.is_displayed(), "Flash messages are not displayed after logout"
        assert "You logged out of the secure area!" in self.page.flash_messages.text, "Logout failed or flash message not as expected"