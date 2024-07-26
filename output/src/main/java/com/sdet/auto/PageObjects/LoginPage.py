
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    txt_username = "#username"
    txt_password = "
    btn_login = ".fa.fa-2x.fa-sign-in"
    lbl_message = "#flash"

    def enter_credentials(self, user_id, password):
        self.page.fill(self.txt_username, user_id)
        self.page.fill(self.txt_password, password)
        self.page.click(self.btn_login)

    def verify_message(self, expected_msg):
        actual_msg = self.page.get_by_selector(self.lbl_message).text_content()
        assert expected_msg in actual_msg, f"Expected message '{expected_msg}' not found in actual message '{actual_msg}'"