from playwright.sync_api import SyncAPIRequestContext
from playwright.sync_api import Page
from playwright.sync_api import Browser
from playwright.sync_api import BrowserContext
from playwright.sync_api import BrowserType

class GuiHelper:
    @staticmethod
    def open_web_browser() -> None:
        browser = SyncAPIRequestContext.launch(headless=False)

    @staticmethod
    def open_web_browser(chrome: Browser) -> None:
        browser = SyncAPIRequestContext.launch(browser_type=chrome, headless=False)

    @staticmethod
    def close_web_browser() -> None:
        browser.close()