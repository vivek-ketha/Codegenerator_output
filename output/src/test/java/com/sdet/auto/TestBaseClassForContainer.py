from playwright.sync_api import Page
from playwright.sync_api import expect
from playwright.sync_api import BrowserType

def test_example(page: Page):
    expect(page).to_have_title("My Test Page")