
from playwright.sync_api import Page

class ForgetPasswordPage:
    def __init__(self, page: Page):
        self.page = page

    txtEmail = "#email"
    btnRetrievePassword = ".icon-2x.icon-signin"

    def enter_email(self, email: str):
        self.page.fill(self.txtEmail, email)

    def click_retrieve_button(self):
        self.page.click(self.btnRetrievePassword)