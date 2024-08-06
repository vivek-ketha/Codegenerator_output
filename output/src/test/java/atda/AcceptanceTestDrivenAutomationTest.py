import pytest
from playwright.sync_api import Page, Playwright

class TestAcceptanceTestDrivenAutomation:
    def setup_class(self):
        self.playwright = Playwright().start()

    def teardown_class(self):
        self.playwright.stop()

    def setup_method(self):
        self.browser = self.playwright.chromium.launch()
        self.page = self.browser.new_page()

    def teardown_method(self):
        self.browser.close()

    def test_should_open(self):
        self.page.goto("https://www.saucedemo.com/")
        assert self.page.url == "https://www.saucedemo.com/"

    def test_should_login(self):
        self.page.goto("https://www.saucedemo.com/")
        self.page.fill("#user-name", "standard_user")
        self.page.fill("#password", "")
        self.page.click("button:has-text('Login')")
        assert self.page.url == "https://www.saucedemo.com/inventory.html"