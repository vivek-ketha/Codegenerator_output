from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def get_user_name_field(self):
        return self.page.locator("#user-name")

    def login(self, user_name, password):
        self.get_user_name_field().fill(user_name)
        self.page.locator("#password").fill(password)
        self.page.locator(".btn_action").click()