
from playwright.sync_api import Page

def nav_to_web_page_under_test(page: Page):
    page.goto(ConfigSettings.get_web_url())