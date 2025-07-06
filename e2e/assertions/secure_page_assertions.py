class SecurePageAssertions:
    def __init__(self, secure_page):
        self.secure_page = secure_page

    def assert_that_user_is_logged_in(self):
        assert self.secure_page.flash_messages.is_displayed(), "Flash messages are not displayed"
        assert "You logged into a secure area!" in self.secure_page.flash_messages.text, ("Login failed or flash "
                                                                                          "message not as expected")
