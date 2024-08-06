from playwright.sync_api import Page, expect

class ShoppingCartPage:
    def __init__(self, page: Page):
        self.page = page

    def get_checkout_button(self):
        return self.page.locator("#FAKE LOCATOR")

    def start_checkout(self):
        self.get_checkout_button().click()