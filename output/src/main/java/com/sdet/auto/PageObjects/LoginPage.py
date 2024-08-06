from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    txt_username = "#username"
    txt_password = "
    btn_login = ".fa.fa-2x.fa-sign-in"
    lbl_message = "#flash"

    def enter_credentials(self, user_id: str, password: str):
        self.page.get_by_selector(self.txt_username).type(user_id)
        self.page.get_by_selector(self.txt_password).type(password)
        self.page.get_by_selector(self.btn_login).click()

    def verify_message(self, test_assert, expected_msg: str):
        message = self.page.get_by_selector(self.lbl_message).text_content()
        test_assert.set_pass(LoggingLibrary.CompareResultContains(message, expected_msg))