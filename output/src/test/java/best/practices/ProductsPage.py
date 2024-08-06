from playwright.sync_api import Page

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page

    def get_shopping_cart_element(self) -> Page:
        return self.page.locator("#BLABHLABHLJ")

    def open_shopping_cart(self) -> None:
        self.get_shopping_cart_element().click()