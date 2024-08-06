from playwright.sync_api import Page, expect

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page

    def is_loaded(self) -> bool:
        element = self.page.locator("#inventory_filter_container")
        return expect(element).to_be_visible().is_ok()