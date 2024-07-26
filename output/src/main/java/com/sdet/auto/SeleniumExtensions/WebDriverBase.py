
from playwright.sync_api import Playwright, Browser, BrowserContext, Page

def get_web_driver(browser: str) -> Page:
    with Playwright() as playwright:
        if browser == "chrome":
            print("Launching Chrome Browser.")
            options = {"headless": False, "args": ["--start-maximized", "--disable-extensions", "disable-infobars"]}
            browser = playwright.chromium.launch(options=options)
            context = browser.new_context()
            page = context.new_page()
            page.set_viewport_size({"width": 1920, "height": 1080})
            return page
        elif browser == "firefox":
            print("Launching Firefox Browser.")
            browser = playwright.firefox.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            page.set_viewport_size({"width": 1920, "height": 1080})
            return page
        elif browser == "seleniumGrid":
            print("Launching Browser Using Selenium Grid - Chrome Browser.")
            browser = playwright.chromium.connect_over_cdp("ws://SESYNPZ6.gridlastic.com:80/wd/hub")
            context = browser.new_context()
            page = context.new_page()
            page.set_viewport_size({"width": 1920, "height": 1080})
            return page
        else:
            raise RuntimeError(f"Browser Type {browser}, not Found, please add additional code for this desired WebDriver Type.")