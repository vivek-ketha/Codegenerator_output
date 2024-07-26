
from playwright.sync_api import Page

class GuiHelper:
    @staticmethod
    def open_web_browser(page: Page):
        page.goto(ConfigSettings.get_web_browser())

    @staticmethod
    def close_web_browser(page: Page):
        page.close()